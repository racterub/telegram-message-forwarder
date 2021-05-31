Telegram Message Forwarder
===

## How to use.
1. Install dependencies
```bash
git clone https://github.com/racterub/telegram-message-forwarder
cd telegram-message-forwarder
pipenv install
```
2. Change the settings
All settings were stored in `config.example.py`.
After modifying it, the filename of `config.example.py` should be changed to `config.py`
```
TOKEN -> The bot's token
USERNAME -> The message sender you want to assign. 
BOT_CHAT_ID = -> The channel you want to be forwarded to. (Format: -xxxxxxxx)
```

3. Run!
```bash
pipenv run python serve.py
```

**This repo is licensed under the MIT license.**