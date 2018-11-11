import json
import subprocess
from telegram.bot import Bot
from telegram.ext import Updater, CommandHandler

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def cmd_runner(command):
    return subprocess.run([command['cmd'], command['args']], stdout=subprocess.PIPE).stdout.decode('utf-8')


class TeleBashBot(Bot):
    def __init__(self, config):
        self.config = {}
        self.load_config(config)
        self.updater = Updater(self.config['bot_token'])
        self.current_cmd_number = -1
        self.add_handlers()

    def add_handlers(self):
        for cmd in self.config['bot_commands']:
            # TODO: Figure out what to do with this shit
            self.current_cmd_number += 1
            self.updater.dispatcher.add_handler(CommandHandler(cmd['telegram_cmd'], self.handler, pass_user_data=True))

    def handler(self, bot, update, user_data):
        current_cmd = self.config['bot_commands'][self.current_cmd_number]['bash_cmd']['cmd']
        current_cmd_args = self.config['bot_commands'][self.current_cmd_number]['bash_cmd']['args']
        cmd = {'cmd': current_cmd, 'args': ' '.join(current_cmd_args)}

        user_data['cmd_result'] = cmd_runner(cmd)
        update.message.reply_text(user_data['cmd_result'])

    def run(self):
        self.updater.start_polling()
        self.updater.idle()

    def load_config(self, config):
        try:
            with open(config) as config:
                self.config = json.load(config)
        except FileNotFoundError:
            print('File does not exist')