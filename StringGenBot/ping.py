import time
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# Replace with your support group link
SUPPORT_CHAT = "https://t.me/MASTIWITHFRIENDSXD"
PING_IMG = "https://files.catbox.moe/520y6h.jpg"  # Replace with your custom image URL

@Client.on_message(filters.command("ping") & filters.private)
async def ping_handler(client: Client, message: Message):
    start = time.time()
    m = await message.reply("🔍 Pinging...")
    end = time.time()
    latency = int((end - start) * 1000)
    
    await m.edit_text(
        f"🏓 Pong!\n⚡ `{latency}ms` response time.",
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
