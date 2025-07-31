from config import MUST_JOIN, START_IMG
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:
        return

    try:
        # Check if user is already a member
        await bot.get_chat_member(MUST_JOIN, msg.from_user.id)

    except UserNotParticipant:
        try:
            # Prepare invite link
            if MUST_JOIN.startswith("-100"):
                chat = await bot.get_chat(MUST_JOIN)
                link = chat.invite_link
                if not link:
                    link = await bot.export_chat_invite_link(MUST_JOIN)
            else:
                link = f"https://t.me/{MUST_JOIN}"

            # Prompt to join
            await msg.reply_photo(
                photo=START_IMG,
                caption=f"""**✦ » ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴏғғɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ ғɪʀsᴛ.**
➲ [🔸 ᴏғғɪᴄᴇ 🔸]({link})

**ᴀғᴛᴇʀ ᴊᴏɪɴɪɴɢ, sᴇɴᴅ /start ᴀɢᴀɪɴ 🌹!**""",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("ᴏғғɪᴄᴇ", url=link)]
                ]),
                parse_mode="Markdown",
                disable_web_page_preview=True
            )
            await msg.stop_propagation()

        except ChatWriteForbidden:
            # Can't send messages to the user
            return

    except ChatAdminRequired:
        print(f"[ERROR] Make sure the bot is admin in MUST_JOIN channel: {MUST_JOIN}")
