import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    # https://my.telegram.org or @usetgxbot
    API_ID = int(os.environ.get("API_ID", 16785))
    API_HASH = os.environ.get("API_HASH")
    
