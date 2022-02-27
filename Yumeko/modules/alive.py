import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Yumeko.events import register as MEMEK
from Yumeko import telethn as tbot

PHOTO = "https://telegra.ph/file/fc8c55424c227e9d2643f.jpg"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  YUMEKO = "**Hello I'm Chrollo!** \n\n"
  YUMEKO += "»**Database is working properly** \n\n"
  YUMEKO += "»**Owner: [[Hunter Committee]](https://t.me/Hunter_Committee), [Freak](https://t.me/Freaking_tag)** \n\n"
  YUMEKO += f"»**Telethon Version : {tlhver}** \n\n"
  YUMEKO += f"»**Pyrogram Version : {pyrover}** \n\n"
  YUMEKO += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/Chrollo_Bot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/Phantom_Troupes")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=YUMEKO,  buttons=BUTTON)

@MEMEK(pattern=("/reload"))
async def reload(event):
  tai = event.sender.first_name
  YUMEKO = "✅ **Chrollo restarted successfully**\n\n• Admin list has been **updated**"
  BUTTON = [[Button.url("📡 ᴜᴘᴅᴀᴛᴇs", "https://t.me/Troupe_Updates")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=YUMEKO,  buttons=BUTTON)
