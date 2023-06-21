import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    ADMIN = os.environ.get("ADMIN") or "6045582180"
    CHANNEL = os.environ.get("CHANNEL") or "EmoijIOS"
    CHANNEKS = os.environ.get("CHANNEKS") or "@EmoijIOS"