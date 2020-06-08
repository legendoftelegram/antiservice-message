#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) king legend

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

from sample_config import Config


import pyrogram
from pyrogram import Client, Message, Filters
logging.getLogger("pyrogram").setLevel(logging.WARNING)

@pyrogram.Client.on_message(pyrogram.Filters.service)
async def service(c: Client, m: Message):
    await c.delete_messages(chat_id=m.chat.id, message_ids=m.message_id)

@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start(c: Client, m: Message):
    await c.send_message(chat_id=m.chat.id, text="**im an anti-service message deletor**")    
