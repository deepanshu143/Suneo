# COPYRIGHT (C) 2021 BY LEGENDX22 AND PROBOYX

"""
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
                 MADE BY LEGENDX AND PROBOYX
                   CREDITS #TEAMLEGEND 
                PLEASE DON'T REMOVE CREDITS
"""

from telethon import events, Button, custom
import re, os
from LEGEND.events import register
from LEGEND import telethn as tbot
from LEGEND import telethn as tgbot
PHOTO = "https://telegra.ph/file/3cc3e9ab5ff0456671ac4.jpg"
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
  BUTTON = [[Button.url("OWNER", "https://t.me/MTY_IZ"), Button.url("MASTER", "https://t.me/LEGENDX22")]]
  BUTTON += [[custom.Button.inline("REPOSITORYS", data="LEGENDX")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LEGENDX,  buttons=BUTTON)




@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"LEGENDX")))
async def callback_query_handler(event):
# inline by LEGENDX22 and PROBOYX🔥
  PROBOYX = [[Button.url("REPO-SUNEO", "https://github.com/Deepanshu143/Suneo"), Button.url("REPO-ULTRA-X", "https://github.com/ULTRA-OP/ULTRA-X")]]
  PROBOYX +=[[Button.url("DEPLOY-SUNEO", "https://heroku.com/deploy?template=https%3A%2F%2Fgithub.com%2Fdeepanshu143%2FSuneo.git"), Button.url("DEPLOY-ULTRA-X", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FULTRA-OP%2FHEROKU&template=https%3A%2F%2Fgithub.com%2FULTRA-OP%2FHEROKU")]]
  PROBOYX +=[[Button.url("TUTORIAL", "https://youtu.be/rGCSSFPsS4Q"), Button.url("STRING-SESSION", "https://repl.it/@legendx22/LEGEND-BOT#main.py")]]
  PROBOYX +=[[Button.url("API_ID & HASH", "https://t.me/usetgxbot"), Button.url("MONGO", "https://mongodb.com")]]
  PROBOYX +=[[Button.url("SUPPORT CHANNEL", "https://t.me/LEGENDBOT_OFFICIAL"), Button.url("SUPPORT GROUP", "https://t.me/LEGEND_USERBOT_SUPPORT")]]
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
  BUTTONS = [[Button.url("MASTER", "https://t.me/LEGENDX22"), Button.url("DEVLOPER", "https://t.me/proboyx")]]
  BUTTONS += [[custom.Button.inline("REPOSITORYS", data="LEGENDX")]]
  await event.edit(text=LEGENDX, buttons=BUTTONS)


@register(pattern=("/repo|/REPO"))
async def repo(event):
  await tbot.send_message(event.chat, "REPO OF SUNEO MANAGER", buttons=[[Button.url("Https://GitHub.com/deepansgu143/suneo")]])
# PROBOYX 🔥 LEGENDX22

__help__ = """
 - /alive check bot alive or die
 - /repo for this bot repo
"""
__mod_name__ = "Alive⚜️"
