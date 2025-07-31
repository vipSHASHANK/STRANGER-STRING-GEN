from config import MUST_JOIN, START_IMG
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:
        return

    try:
        # Check if the user is a member of the MUST_JOIN channel
        await bot.get_chat_member(MUST_JOIN, msg.from_user.id)

    except UserNotParticipant:
        try:
            # Generate channel link (username or invite)
            if MUST_JOIN.startswith("-100"):
                chat = await bot.get_chat(MUST_JOIN)
                link = chat.invite_link
                if not link:
                    link = await bot.export_chat_invite_link(MUST_JOIN)
            else:
                link = f"https://t.me/{MUST_JOIN}"

            # Send join prompt
            await msg.reply_photo(
                photo=START_IMG,
                caption=f"""✦ » ғɪʀsᴛʟʏ ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ᴏᴜʀ ғᴀᴍɪʟʏ ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ.

➲ [🔸 ᴏғғɪᴄᴇ 🔸]({link})

ᴀғᴛᴇʀ ᴊᴏɪɴɪɴɢ ❖ /start ❖ ᴍᴇ ᴀɢᴀɪɴ 🌹!""",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("ᴏғғɪᴄᴇ", url=link)]
                ]),
                disable_web_page_preview=True
            )
            await msg.stop_propagation()

        except ChatWriteForbidden:
            # Bot can't write in private chat
            return

    except ChatAdminRequired:
        print(f"[ERROR] Promote the bot as admin in MUST_JOIN chat: {MUST_JOIN}")
