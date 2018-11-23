import json
import subprocess

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.bot import Bot
from telegram.ext import Updater, CommandHandler

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def cmd_runner(command):
    return subprocess.run([command['cmd'], command['args']], stdout=subprocess.PIPE).stdout.decode('utf-8')


class TeleBashBot:
    def __init__(self, config):
        self.config = {}
        try:
            self.load_config(config)
            self.updater = Updater(self.config['bot_token'])
            self.add_handlers()
        except FileNotFoundError:
            print('File does not exist')

    def get_current_cmd(self, user_text):
        cmd = list(filter(lambda cmd: cmd['telegram_cmd'] == user_text.replace('/', ''), self.config['bot_commands']))

        if cmd[0]['type'] == 'tg_keyboard':
            buttons = cmd[0]['buttons']
            cmd = {'cmd_type': 'keyboard_markup', 'buttons': buttons}
        else:
            current_cmd = cmd[0]['bash_cmd']['cmd']
            current_cmd_args = cmd[0]['bash_cmd']['args']
            cmd = {'cmd_type': 'bash_command', 'cmd': current_cmd, 'args': ' '.join(current_cmd_args)}
        return cmd

    def add_handlers(self):
        for cmd in self.config['bot_commands']:
            handler = None
            pass_user_data = True
            if cmd['type'] == 'tg_cmd':
                handler = self.handler
                pass_user_data = True
            elif cmd['type'] == 'tg_keyboard':
                handler = self.keyboard_layout_handler
                pass_user_data = False

            self.updater.dispatcher.add_handler(CommandHandler(cmd['telegram_cmd'], handler, pass_user_data=pass_user_data))

    def handler(self, bot, update, user_data):
        cmd = self.get_current_cmd(update.message.text)
        user_data['cmd_result'] = cmd_runner(cmd)
        update.message.reply_text(user_data['cmd_result'])

    def keyboard_layout_handler(self, bot, update):
        cmd = self.get_current_cmd(update.message.text)

        keyboard = [
            [InlineKeyboardButton(btn['caption'], callback_data='1') for btn in cmd['buttons']]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text('Available commands: ', reply_markup=reply_markup)

    def run(self):
        self.updater.start_polling()
        self.updater.idle()

    def load_config(self, config):
        with open(config) as config:
            self.config = json.load(config)