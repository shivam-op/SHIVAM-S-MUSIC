from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Hey, π'πΊ β¨ SHIVAM'π¦ π π¨π¦ππ π£πππ¬ππ₯ β’ β¨
I can play music in your group's voice call. Developed by [SHIVAM](https://t.me/SHIVAM9412).
Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π₯BOT MAKERπ₯", url="https://t.me/SHIVAM9412")
                  ],[
                    InlineKeyboardButton(
                        "π₯GROUPπ₯", url="https://t.me/WINZOGOLD_DISCUSS"
                    ),
                    InlineKeyboardButton(
                        "π₯COMMANDS π₯", url="https://telegra.ph/MusicBot-Robot-MusicBot-Robo-03-14"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "π₯ ADD TO YOUR GROUP π₯", url="https://t.me/WINZO_VC_BOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**β¨ SHIVAM β¨ is on fire π₯ β**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "πΏπ»π°ππΈπ½πΆ π±π ππΎππ π€π»", url="https://t.me/SHIVAM9412")
                ]
            ]
        )
   )

