# TeleBash [![Build Status](https://travis-ci.com/sadmonad/TeleBash.svg?branch=master)](https://travis-ci.com/sadmonad/TeleBash)

## Installation

Download the repo & simply run: `pip3 install -r requirements.txt`

## Using
Just set up your config file like following:
```json
{
  "bot_token": "", // Your bot token from BotFather,
  "chat_id": "",   // User id
  "bot_commands":
  [
    {
      "telegram_cmd": "uname",
      "bash_cmd":
      {
        "use_sudo": false,
        "cmd": "uname",
        "args": ["-r"]
      },
      "description": "Shows short kernel info"
    }
  ]
}
```

And then run bot:
```python
from TeleBash.core.bot.Bot import TeleBashBot


BOT_CONFIG_PATH = './default_config.json'
bot = TeleBashBot(BOT_CONFIG_PATH)
bot.run()
```