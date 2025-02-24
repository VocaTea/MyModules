# ---------------------------------------------------------------------------------
#░█▀▄░▄▀▀▄░█▀▄░█▀▀▄░█▀▀▄░█▀▀▀░▄▀▀▄░░░█▀▄▀█
#░█░░░█░░█░█░█░█▄▄▀░█▄▄█░█░▀▄░█░░█░░░█░▀░█
#░▀▀▀░░▀▀░░▀▀░░▀░▀▀░▀░░▀░▀▀▀▀░░▀▀░░░░▀░░▒▀
# Name: hent
# Description: words superfluous?
# Author: @VocaTea
# ---------------------------------------------------------------------------------
# 🔒    Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# ---------------------------------------------------------------------------------
# Author: @VocaTea
# scope: hikka_only
# meta developer: @codrago_m
# ---------------------------------------------------------------------------------
#commands: nsfw
__version__ = (1, 0, 1)
import os
import logging
from .. import loader, utils
import random
import time
import datetime
from telethon import functions
from telethon.tl.custom import Message

logger = logging.getLogger("HentaiRoulet")

@loader.tds
class HentaiRoulet(loader.Module):
    """Hentai roulet"""
    strings = {
        "name": "HentaiRoulet",
        "search": "<emoji document_id=5368580099182435492>👁</emoji> loading your Hentai..."
    }
    
    async def nsfwcmd(self, message: Message):
         """-> to get your nsfw arts"""
         await message.edit(self.strings("search"))
         time.sleep(0.5)
         chat = "spin_nsfw"
         result = await message.client(
             functions.messages.GetHistoryRequest(
                 peer=chat,
                 offset_id=0,
                 offset_date=datetime.datetime.now(),
                 add_offset=random.choice(range(1, 660, 2)),
                 limit=1,
                 max_id=0,
                 min_id=0,
                 hash=0,
             ),
         )
         await message.delete()
         await message.client.send_file(
             message.to_id, 
             result.messages[0].media, 
             reply_to=getattr(message, "reply_to_msg_id", None),
         )
