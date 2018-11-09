from telegram.bot import Bot


class TeleBashBot(Bot):

    def __init__(self, config):
        self.config = config
        super().__init__(self.token)

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