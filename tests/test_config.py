import unittest
from TeleBash.core.bot.Bot import TeleBashBot
from TeleBash.core.exceptions import ConfigUniqueTelegramCommandsError

TEST_CONFIG_PATH = './test_config.json'
WRONG_CONFIG_PATH = '/wrong_path'


class ConfigTest(unittest.TestCase):

    def parse_config(self, config_path):
        self.bot = TeleBashBot(config_path)

    def test_file_does_not_exist(self):
        self.assertRaises(FileNotFoundError, self.parse_config(WRONG_CONFIG_PATH))

    def test_config_unique_telegram_commands(self):
        with self.assertRaises(SystemExit):
            self.parse_config(TEST_CONFIG_PATH)


if __name__ == '__main__':
    unittest.main()
