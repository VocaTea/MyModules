#commands: nlh
__version__ = (1 , 0)
import os
import logging
from .. import loader, utils
import random
import time
import datetime
from telethon import functions
from telethon.tl.custom import Message

logger = logging.getLogger("рулетка")

@loader.tds
class рулетка(loader.Module):
    """Anime arts roulet"""
    strings = {
        "name": "Рулетка",
        "search": "<emoji document_id=5188311512791393083>🔎</emoji> search your art..."
    }
    
    async def nlhcmd(self, message: Message):
         """-> to get your arts"""
         await message.edit(self.strings("search"))
         time.sleep(0.5)
         chat = "Kkkain"
         result = await message.client(
             functions.messages.GetHistoryRequest(
                 peer=chat,
                 offset_id=0,
                 offset_date=datetime.datetime.now(),
                 add_offset=random.choice(range(1, 1420, 4)),
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
