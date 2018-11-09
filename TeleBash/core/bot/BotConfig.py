import json


class BotConfig:
    def __init__(self, config_path):
        try:
            with open(config_path) as config:
                self.config = json.load(config)
        except FileNotFoundError:
            print("Specified file doesn't exist")