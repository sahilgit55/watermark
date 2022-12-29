# (c) @AbirHasan2005

import asyncio
from configs import Config
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import enums



async def handle_force_subscribe(bot, cmd):
    try:
        user = await bot.get_chat_member(int(Config.UPDATES_CHANNEL), cmd.chat.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=cmd.chat.id,
                text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/linux_repo).",
                parse_mode=enums.ParseMode.MARKDOWN,
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:
        try:
            invite_link = await bot.create_chat_invite_link(int(Config.UPDATES_CHANNEL))
        except FloodWait as e:
            await asyncio.sleep(e.x)
            return 400
        await bot.send_message(
            chat_id=cmd.chat.id,
            text="**Please Join My Updates Channel to use this Bot!**\n\nDue to Overload, Only Channel Subscribers can use the Bot!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤖 Join Updates Channel", url=invite_link.invite_link)
                    ],
                    [
                        InlineKeyboardButton("🔄 Refresh 🔄", callback_data="refreshmeh")
                    ]
                ]
            ),
            parse_mode=enums.ParseMode.MARKDOWN
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.chat.id,
            text="Something went Wrong. Contact my [Support Group](https://t.me/linux_repo).",
            parse_mode=enums.ParseMode.MARKDOWN,
            disable_web_page_preview=True
        )
        return 400
