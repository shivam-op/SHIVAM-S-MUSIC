from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Hey, 𝗜'𝗺 ✨ SHIVAM'𝗦 𝗠𝗨𝗦𝗜𝗖 𝗣𝗟𝗔𝗬𝗘𝗥 ™ ✨
I can play music in your group's voice call. Developed by [SHIVAM](https://t.me/SHIVAM9412).
Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🤞🏻𝚈𝙾𝚄𝚁 𝙼𝙰𝙺𝙴𝚁🤞🏻", url="https://t.me/SHIVAM9412")
                  ],[
                    InlineKeyboardButton(
                        "🔰𝙶𝚁𝙾𝚄𝙿🔰", url="https://t.me/WINZOGOLD_DISCUSS"
                    ),
                    InlineKeyboardButton(
                        "🎛️ 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 🎛️", url="https://telegra.ph/MusicBot-Robot-MusicBot-Robo-03-14"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "😎 𝙰𝙳𝙳 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 😎", url="https://t.me/WINZO_VC_BOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**✨ SHIVAM ✨ is on fire 🔥 ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙿𝙻𝙰𝚈𝙸𝙽𝙶 𝙱𝚈 𝚈𝙾𝚄𝚁 🤙🏻", url="https://t.me/SHIVAM9412")
                ]
            ]
        )
   )

