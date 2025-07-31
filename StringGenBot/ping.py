import time
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# Custom Links
SUPPORT_CHAT = "https://t.me/MASTIWITHFRIENDSXD"
PING_IMG = "https://files.catbox.moe/520y6h.jpg"  # Custom image link

# Uptime tracker
BOT_START_TIME = time.time()

def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "d"]

    while count < 4 and seconds > 0:
        count += 1
        remainder, result = divmod(int(seconds), 60) if count < 3 else divmod(int(seconds), 24)
        if result != 0:
            time_list.append(f"{result}{time_suffix_list[count - 1]}")
        seconds = remainder

    return ":".join(reversed(time_list))


@Client.on_message(filters.command("ping") & filters.private)
async def ping_handler(client: Client, message: Message):
    start = time.time()
    temp = await message.reply("💫 Pinging...")
    end = time.time()
    latency = (end - start) * 1000
    uptime = get_readable_time(time.time() - BOT_START_TIME)

    await temp.delete()

    await message.reply_photo(
        photo=PING_IMG,
        caption=f"""⊚ ʜᴇʏ ʙᴀʙʏ !!
˹ 𝛅ᴛʀɪηɢ ꭙ ɢєηєʀᴧᴛσʀ ˼ ɪꜱ ᴀʟɪᴠᴇ 🥀 ᴀɴᴅ ᴡᴏʀᴋɪɴɢ ғɪɴᴇ

➥ ᴘᴏɴɢ: `{latency:.3f} ms`
➥ ᴜᴘᴛɪᴍᴇ: {uptime}

⦿ ᴄʀᴇᴀᴛᴇᴅ ʙʏ ᴀʟᴘʜᴀ-ʙᴀʙʏ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🔸 Support", url=SUPPORT_CHAT)],
                [InlineKeyboardButton("❌ Close", callback_data="close_ping")]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close_ping"))
async def close_ping_cb(_, query: CallbackQuery):
    try:
        await query.message.delete()
    except:
        await query.answer("❌ Can't delete", show_alert=True)
