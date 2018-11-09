import unittest
from TeleBash.core.bot.BotConfig import BotConfig


class ConfigTest(unittest.TestCase):
    def parse_config(self, config_path):
        self.bot = BotConfig(config_path)

    def test_file_does_not_exist(self):
        self.assertRaises(FileNotFoundError, self.parse_config('/wrong_path'))


if __name__ == '__main__':
    unittest.main()