# COPYRIGHT BY PARTH
# ALL RIGHTS RESERVED


import asyncio

from random import choice

from pyrogram import filters, Client
from pyrogram.types import Message

from data import OneWord, RAID, THE_ALTS
from config import SUDO_USERS


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], [".", "/", "!"]))
async def dmraid(xcrazy: Client, message: Message):
      alt = message.text.split(" ")

      if len(alt) == 3:
          ok = await xcrazy.get_users(alt[2])
          id = ok.id

          if id in THE_ALTS:
                await message.reply_text(f"`ᴠᴇʀɪғɪᴇᴅ ʙʏ ᴄʀᴀ𝐙ʏ P ᴀ ʀ ᴛ ʜ `")
          elif id in SUDO_USERS:
                await message.reply_text(f"`ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴍʏ sᴜᴅᴏ ᴜsᴇʀ`")
          else:
              counts = int(alt[1])
              await message.reply_text("`ᴅᴍ ʀᴀɪᴅ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ`")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await xcrazy.send_message(id, msg)
                    await asyncio.sleep(0.1)

      elif message.reply_to_message and (len(alt) == 2):
          user_id = message.reply_to_message.from_user.id
          ok = await xcrazy.get_users(user_id)
          id = ok.id

          if id in THE_ALTS:
                await message.reply_text(f"`ᴠᴇʀɪғɪᴇᴅ ʙʏ ᴄʀᴀ𝐙ʏ P ᴀ ʀ ᴛ ʜ`")
          elif id in SUDO_USERS:
                await message.reply_text(f"`ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴍʏ sᴜᴅᴏ ᴜsᴇʀ`")
          else:
              counts = int(alt[1])
              await message.reply_text("`ᴅᴍ ʀᴀɪᴅ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ`")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await xcrazy.send_message(id, msg)
                    await asyncio.sleep(0.1)

      else:
            await message.reply_text("⚡ ᴜsᴀɢᴇ:\n   !dmraid 13 <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ>")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], [".", "!", "/"]))
async def dmspam(client: Client, message: Message):
    alt = message.text.split(" ", 3)

    if  len(alt) == 4:
        uid = int(alt[2])
        if uid in THE_ALTS:
            await message.reply_text(f"`ᴠᴇʀɪғɪᴇᴅ ʙʏ ᴀʟᴛʀᴏɴ x`")
        elif uid in SUDO_USERS:
            await message.reply_text(f"`ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴍʏ sᴜᴅᴏ ᴜsᴇʀ`")
        else:
            quantity, spam_text = int(alt[1]), alt[3]
            await message.reply_text("`ᴅᴍ ꜱᴘᴀᴍ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ`")
            for _ in range(quantity):
                await client.send_message(uid, spam_text)
                await asyncio.sleep(0.3)

    elif message.reply_to_message and (len(alt) == 3):
        id = message.reply_to_message.from_user.id

        if id in THE_ALTS:
            await message.reply_text(f"`ᴠᴇʀɪғɪᴇᴅ ʙʏ ᴀʟᴛʀᴏɴ x`")
        elif id in SUDO_USERS:
            await message.reply_text(f"`ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴍʏ sᴜᴅᴏ ᴜsᴇʀ`")
        else:
            quantity = int(alt[1])
            spam_text = alt[2]
            await message.reply_text("`ᴅᴍ ꜱᴘᴀᴍ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ`")
            for _ in range(quantity):
                await client.send_message(id, spam_text)
                await asyncio.sleep(0.3)

    else:
        await message.reply_text("😈 ᴜsᴀɢᴇ:\n .dmspam 13 <ᴜꜱᴇʀ ɪᴅ> Altron\n .dmspam 13 Altron <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>")
