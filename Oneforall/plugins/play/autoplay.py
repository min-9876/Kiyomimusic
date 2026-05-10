import random

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup

import config
from config import BANNED_USERS, lyrical
from Oneforall import YouTube, app
from Oneforall.utils.database import (
    is_autoplay_on,
    get_autoplay_mood,
    set_autoplay,
    set_autoplay_mood,
)
from Oneforall.utils.decorators.language import languageCB
from Oneforall.utils.inline import (
    autoplay_mood_markup,
    autoplay_language_markup,
)
from Oneforall.misc import db


# Store previous tracks per chat
previous_tracks = {}


@app.on_message(filters.command("songconfig") & filters.group & ~BANNED_USERS)
@languageCB
async def songconfig_command(client, message, _):
    """Command to configure autoplay with mood and language"""

    await message.reply_text(
        "🎵 **ᴀᴜᴛᴏᴘʟᴀʏ ᴄᴏɴғɪɢᴜʀᴀᴛɪᴏɴ**\n\n"
        "sᴇʟᴇᴄᴛ ʏᴏᴜʀ ᴘʀᴇғᴇʀʀᴇᴅ ᴍᴏᴏᴅ:",
        reply_markup=autoplay_mood_markup(),
    )


@app.on_callback_query(filters.regex(r"^songconfig_mood:"))
@languageCB
async def handle_mood_selection(client, CallbackQuery, _):
    """Handle mood selection callback"""

    chat_id = CallbackQuery.message.chat.id

    try:
        mood = CallbackQuery.data.split(":", 1)[1]
    except Exception:
        return await CallbackQuery.answer(
            "ɪɴᴠᴀʟɪᴅ ᴍᴏᴏᴅ sᴇʟᴇᴄᴛɪᴏɴ",
            show_alert=True,
        )

    # Temporary store
    if chat_id not in lyrical:
        lyrical[chat_id] = {}

    lyrical[chat_id]["autoplay_mood"] = mood

    await CallbackQuery.edit_message_text(
        f"🎵 **ᴍᴏᴏᴅ sᴇʟᴇᴄᴛᴇᴅ:** `{mood.title()}`\n\n"
        "ɴᴏᴡ sᴇʟᴇᴄᴛ ʏᴏᴜʀ ᴘʀᴇғᴇʀʀᴇᴅ ʟᴀɴɢᴜᴀɢᴇ:",
        reply_markup=autoplay_language_markup(),
    )


@app.on_callback_query(filters.regex(r"^songconfig_language:"))
@languageCB
async def handle_language_selection(client, CallbackQuery, _):
    """Handle language selection callback"""

    chat_id = CallbackQuery.message.chat.id

    try:
        language = CallbackQuery.data.split(":", 1)[1]
    except Exception:
        return await CallbackQuery.answer(
            "ɪɴᴠᴀʟɪᴅ ʟᴀɴɢᴜᴀɢᴇ sᴇʟᴇᴄᴛɪᴏɴ",
            show_alert=True,
        )

    if chat_id not in lyrical:
        lyrical[chat_id] = {}

    mood = lyrical[chat_id].get("autoplay_mood", "chill")

    # Save settings
    await set_autoplay(chat_id, True)

    await set_autoplay_mood(
        chat_id,
        {
            "mood": mood,
            "language": language,
        },
    )

    # Cleanup temp cache
    lyrical[chat_id].pop("autoplay_mood", None)

    await CallbackQuery.edit_message_text(
        "✅ **ᴀᴜᴛᴏᴘʟᴀʏ ᴇɴᴀʙʟᴇᴅ**\n\n"
        f"🎵 ᴍᴏᴏᴅ: `{mood.title()}`\n"
        f"🌐 ʟᴀɴɢᴜᴀɢᴇ: `{language.title()}`\n\n"
        "ʙᴏᴛ ᴡɪʟʟ ɴᴏᴡ ᴘʟᴀʏ sᴏɴɢs ʙᴀsᴇᴅ ᴏɴ ʏᴏᴜʀ sᴇʟᴇᴄᴛᴇᴅ ᴘʀᴇғᴇʀᴇɴᴄᴇs."
    )


@app.on_callback_query(filters.regex(r"^AutoPlay"))
@languageCB
async def toggle_autoplay(client, CallbackQuery, _):
    """Toggle autoplay on/off"""

    callback_data = CallbackQuery.data.strip()

    try:
        chat_id = int(callback_data.split("|")[1])
    except Exception:
        return await CallbackQuery.answer(
            "ɪɴᴠᴀʟɪᴅ ᴄʜᴀᴛ ɪᴅ",
            show_alert=True,
        )

    autoplay_status = await is_autoplay_on(chat_id)

    if autoplay_status:
        await set_autoplay(chat_id, False)

        return await CallbackQuery.edit_message_text(
            "❌ **ᴀᴜᴛᴏᴘʟᴀʏ ᴅɪsᴀʙʟᴇᴅ**"
        )

    await CallbackQuery.edit_message_text(
        "🎵 **ᴇɴᴀʙʟᴇ ᴀᴜᴛᴏᴘʟᴀʏ**\n\n"
        "sᴇʟᴇᴄᴛ ʏᴏᴜʀ ᴘʀᴇғᴇʀʀᴇᴅ ᴍᴏᴏᴅ:",
        reply_markup=autoplay_mood_markup(),
    )


async def get_autoplay_recommendation(chat_id: int, user_id: int):
    """Get autoplay song recommendation"""

    if chat_id not in previous_tracks:
        previous_tracks[chat_id] = []

    mood_data = await get_autoplay_mood(chat_id)

    mood = "chill"
    language = "english"

    if isinstance(mood_data, dict):
        mood = mood_data.get("mood", "chill")
        language = mood_data.get("language", "english")

    query = f"{mood} {language} songs"

    try:
        track_data, track_id = await YouTube.track(query)

        if not track_data or not track_id:
            return None, None

        if len(previous_tracks[chat_id]) >= 10:
            previous_tracks[chat_id].pop(0)

        previous_tracks[chat_id].append(
            {
                "title": track_data.get("title"),
                "vidid": track_id,
                "mood": mood,
                "language": language,
            }
        )

        return track_data, track_id

    except Exception as e:
        print(f"Autoplay Error: {e}")
        return None, None
