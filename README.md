# TeleBash [![Build Status](https://travis-ci.com/sadmonad/TeleBash.svg?branch=master)](https://travis-ci.com/sadmonad/TeleBash)

## Installation

Download the repo & simply run: `python setup.py install`

## Using
Just set up your config file like following:
```json
{
  "bot_token": "" ,
  "user_id": "",
  "bot_commands":
  [
    {
      "type": "tg_keyboard",
      "telegram_cmd": "start",
      "buttons":
      [
        {
          "caption": "Kernel",
          "action":
          {
            "type": "tg_cmd",
            "telegram_cmd": "kernel",
            "bash_cmd":
            {
              "use_sudo": false,
              "cmd": "uname",
              "args": ["-r"]
            }
          }
        },
        {
          "caption": "Files",
          "action":
          {
            "type": "tg_cmd",
            "telegram_cmd": "files",
            "bash_cmd":
            {
              "use_sudo": false,
              "cmd": "ls",
              "args": ["-l"]
            }
          }
        }
      ],
      "description": "Shows short kernel info"
    },
    {
      "type": "tg_cmd",
      "telegram_cmd": "moo",
      "bash_cmd":
      {
        "use_sudo": false,
        "cmd": "apt-get",
        "args": ["moo"]
      },
      "description": "Shows cow"
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