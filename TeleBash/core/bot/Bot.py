import json
from telegram.bot import Bot
from telegram.ext import Updater, CommandHandler

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


class TeleBashBot(Bot):
    def __init__(self, config):
        self.config = {}
        self.load_config(config)
        self.updater = Updater(self.config['bot_token'])
        self.add_handlers()

    def add_handlers(self):
        for cmd in self.config['bot_commands']:
            self.updater.dispatcher.add_handler(CommandHandler(cmd['telegram_cmd'],
                                                              lambda bot, update:
                                                              update.message.reply_text(cmd['description'])))

    def run(self):
        self.updater.start_polling()
        self.updater.idle()

    def load_config(self, config):
        try:
            with open(config) as config:
                self.config = json.load(config)
        except FileNotFoundError:
            print('File does not exist')

    def send_message(self,
                     chat_id,
                     text,
                     parse_mode=None,
                     disable_web_page_preview=None,
                     disable_notification=False,
                     reply_to_message_id=None,
                     reply_markup=None,
                     timeout=None,
                     **kwargs):
        super().send_message(chat_id, text)

    def reload_config(self, config):
        raise NotImplementedError

    def send_document(self,
                      chat_id,
                      document,
                      filename=None,
                      caption=None,
                      disable_notification=False,
                      reply_to_message_id=None,
                      reply_markup=None,
                      timeout=20,
                      parse_mode=None,
                      thumb=None,
                      **kwargs):
        super().send_document(chat_id, document)