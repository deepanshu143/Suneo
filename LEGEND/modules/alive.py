# COPYRIGHT (C) 2021 BY LEGENDX22 AND PROBOYX

"""
(((((((((((((((((((((((@doreamonfans1)))))))))))))))))))))))))))
(((((((((((((((((((((((@doreamonfans2)))))))))))))))))))))))))))
(((((((((((((((((((((((@doreamonfans4)))))))))))))))))))))))))))
(((((((((((((((((((((((@doreamonfans5)))))))))))))))))))))))))))
                 MADE BY Doreamonfans
                   CREDITS #TEAMLEGEND 
                PLEASE DON'T REMOVE CREDITS
"""

from telethon import events, Button, custom
import re, os
from LEGEND.events import register
from LEGEND import telethn as tbot
from LEGEND import telethn as tgbot
PHOTO = "https://telegra.ph/file/f7355bc6002e744effe94.jpg"
@register(pattern=("/alive"))
async def awake(event):
  legendx = event.sender.first_name
  LEGENDX = "HELLO THIS IS Suneo Manager \n\n"
  LEGENDX += "ALL SYSTEM WORKING PROPERLY\n\n"
  LEGENDX += "GRAND OS : 3.8 LATEST\n\n"
  LEGENDX += f"MY MASTER {legendx} ☺️\n\n"
  LEGENDX += "FULLY UPDATED\n\n"
  LEGENDX += "TELETHON : 1.19.5 LATEST\n\n"
  LEGENDX += "THANKS FOR ADD ME HERE"
  BUTTON = [[Button.url("OWNER", "https://t.me/doreamonfans2"), Button.url("MASTER", "https://t.me/doreamonfans1")]]
  BUTTON += [[custom.Button.inline("REPOSITORYS", data="LEGENDX")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=Doreamonfans,  buttons=BUTTON)




@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"LEGENDX")))
async def callback_query_handler(event):
# inline by LEGENDX22 and PROBOYX🔥
  PROBOYX = [[Button.url("owner 1", "https://t.me/doreamonfans1"), Button.url("owner 2", "https://t.me/doreamonfans2")]]
  PROBOYX +=[[Button.url("owner 3", "https://t.me/doreamonfans4"), Button.url("owner 4","https://t.me/doreamonfans5)]]
  PROBOYX +=[[Button.url("UPDATES CHANNEL", "https://t.me/disneygrou"), Button.url("SUPPORT GROUP", "https://t.me/disneyteamchat")]]
  PROBOYX +=[[custom.Button.inline("ALIVE", data="PROBOY")]]
  await event.edit(text=f"ALL DETAILS OF REPOS", buttons=PROBOYX)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"PROBOY")))
async def callback_query_handler(event):
  global PHOTO
  legendx = event.sender.first_name
# inline by LEGENDX22 and PROBOYX 🔥
  LEGENDX = "HELLO THIS IS SUNEO MANAGER \n\n"
  LEGENDX += "ALL SYSTEM WORKING PROPERLY\n\n"
  LEGENDX += "GRAND OS : 3.8 LATEST\n\n"
  LEGENDX += f"MY MASTER {legendx} ☺️\n\n"
  LEGENDX += "FULLY UPDATED BOT\n\n"
  LEGENDX += "TELETHON : 1.19.5 LATEST\n\n"
  LEGENDX += "THANKS FOR ADD ME HERE"
  BUTTONS = [[Button.url("MASTER", "https://t.me/doreamonfans2"), Button.url("DEVLOPER", "https://t.me/doreamonfans1")]]
  BUTTONS += [[custom.Button.inline("REPOSITORYS", data="LEGENDX")]]
  await event.edit(text=LEGENDX, buttons=BUTTONS)


@register(pattern=("/repo|/REPO"))
async def repo(event):
  await tbot.send_message(event.chat, "REPO OF SUNEO MANAGER AS OWNER", buttons=[[Button.url("⚜️OWNER⚜️", "https://t.me/doreamonfans2")]])
# PROBOYX 🔥 Doreamonfans

__help__ = """
 - /alive check bot alive or die
 - /repo for this bot repo
"""
__mod_name__ = "Alive⚜️"
