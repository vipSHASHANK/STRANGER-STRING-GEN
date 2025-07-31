from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from config import *

START_TXT = """✦ » ʜᴇʏ  {msg.from_user.mention}  ✤,
✦ » ɪ ᴀᴍ {me2},

✦ » Aɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

✦ » ᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ᴘʏᴛʜᴏɴ ʟɪʙʀᴀʀʏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ꜰᴏʀ.

✦ » ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴀɴʏ ʜᴇʟᴘ, ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ !"""

START_BTN =             [InlineKeyboardButton("ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ", callback_data="generate")],
                [
                    InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/MASTIWITHFRIENDSXD"),
                    InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://tg://user?id={OWNER_ID}")
                ],
                [InlineKeyboardButton("📘 ɢᴜɪᴅᴇ", cack_data="guide")]
            ]

GUIDE_TXT ="""✦ ʙᴀsɪᴄ ᴄᴏᴍᴍᴀɴᴅs

➻ ᴛʏᴘᴇ /gen ᴏʀ ᴛᴀᴘ ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ ғᴏʀ ɢᴇɴ sᴇssɪᴏɴ.

➻ ᴛʏᴘᴇ /ping ᴄʜᴇᴄᴋ ʙᴏᴛ ᴜᴘᴛɪᴍᴇ
➻ ᴛʏᴘᴇ /stats ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ʙᴏᴛ sᴛᴀᴛs

➻ ᴛʏᴘᴇ /broadcast ᴛᴏ sᴇɴᴅ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜsᴇʀs + ᴄʜᴀᴛs (ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴜsᴇ)

⦿ ᴊᴏɪɴ sᴜᴘᴘᴏʀᴛ ғᴏʀ ᴍᴏʀᴇ ᴜᴘᴅᴀᴛᴇs."""


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_photo(
        chat_id=msg.chat.id,
        photo=START_IMG,
        caption=START_TXT,
        reply_markup=InlineKeyboardMarkup(START_BTN),
    )

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    data = query.data

    if data == "guide":
        await query.message.edit_text(
            text="""✦ ʙᴀsɪᴄ ᴄᴏᴍᴍᴀɴᴅs

➻ ᴛʏᴘᴇ /gen ᴏʀ ᴛᴀᴘ ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ ғᴏʀ ɢᴇɴ sᴇssɪᴏɴ.

➻ ᴛʏᴘᴇ /ping ᴄʜᴇᴄᴋ ʙᴏᴛ ᴜᴘᴛɪᴍᴇ
➻ ᴛʏᴘᴇ /stats ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ʙᴏᴛ sᴛᴀᴛs

➻ ᴛʏᴘᴇ /broadcast ᴛᴏ sᴇɴᴅ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜsᴇʀs + ᴄʜᴀᴛs (ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴜsᴇ)

⦿ ᴊᴏɪɴ sᴜᴘᴘᴏʀᴛ ғᴏʀ ᴍᴏʀᴇ ᴜᴘᴅᴀᴛᴇs.""",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⬅️ ʙᴀᴄᴋ", callback_data="start_menu")]]
            )
        )

    elif data == "start_menu":
        me2 = (await client.get_me()).mention
        await query.message.edit_caption(
            caption=START_TXT,
            reply_markup=InlineKeyboardMarkup(START_BTN)
        )
