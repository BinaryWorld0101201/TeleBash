from telegram import Message


class Command(Message):
    def __init__(self):
        super().__init__(message_id, from_user, date, chat)