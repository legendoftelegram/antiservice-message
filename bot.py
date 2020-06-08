#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) king legend

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

from sample_config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "deleter",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    app.run()
