# COPYRIGHT BY PARTH
# ALL RIGHTS RESERVED

import sys
import datetime

from os import execle, environ
from config import ALIVE_PIC, SUDO_USERS

from pyrogram import Client, filters
from pyrogram.types import Message


ALT = f"""❖ 𝐏𝐘  P ᴀ ʀ ᴛ ʜ  ❖

➠ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.11.1`
➠ **ᴘʏʀᴏ ᴠᴇʀsɪᴏɴ** : `1.4.16`
➠ **x🇨 🇷 🇦 🇿 🇾  ᴠᴇʀsɪᴏɴ**  : `3.3`
➠ **ᴜᴘᴅᴀᴛᴇꜱ** : @crazyXparth\"""


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], ["/", ".", "!"]))
async def ping(_, e: Message):       
      start = datetime.datetime.now()
      Fuk = await e.reply("**Pong !!**")
      end = datetime.datetime.now()
      ms = (end-start).microseconds / 1000
      await Fuk.edit_text(f"◇ ᴛʜᴇ 🇨 🇷 🇦 🇿 🇾  \n◇ ᴘɪɴɢ: `{ms}ms`\n◇ ᴠᴇʀsɪᴏɴ: `3.3`")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], ["/", ".", "!"]))
async def alive(xcrazy: Client, msg: Message):
       if ".jpg" in ALIVE_PIC or ".png" in ALIVE_PIC:
              await xcrazy.send_photo(msg.chat.id, ALIVE_PIC, caption=ALT)
       if ".mp4" in ALIVE_PIC or ".MP4," in ALIVE_PIC:
              await xcrazy.send_video(msg.chat.id, ALIVE_PIC, caption=ALT)


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["reboot", "restart"], ["/", ".", "!"]))
async def restart_bot(_, message: Message):
    msg = await message.reply("`ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ...`")
    args = [sys.executable, "main.py"]
    await msg.edit("» ʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ...\n» ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ ᴀғᴛᴇʀ 𝟷 ᴍɪɴᴜᴛᴇ ")
    execle(sys.executable, *args, environ)