import asyncio
from datetime import datetime
from logging import getLogger

from pyrogram import filters
from pyrogram.types import Message
from pyrogram.raw import functions
from pytgcalls import PyTgCalls
from pytgcalls.types import Update

from Oneforall import app, userbot  # Aapka userbot/assistant instance
from Oneforall.utils.database import get_assistant

LOGGER = getLogger(__name__)

# PyTgCalls client ko assistant account ke sath initialize kiya
pytgcalls_client = PyTgCalls(userbot)


# ───────── SMALL CAPS ─────────
def to_small_caps(text: str):
    if not text:
        return ""
    mapping = {
        "a":"ᴀ","b":"ʙ","c":"ᴄ","d":"ᴅ","e":"ᴇ","f":"ꜰ","g":"ɢ","h":"ʜ","i":"ɪ","j":"ᴊ",
        "k":"ᴋ","l":"ʟ","m":"ᴍ","n":"ɴ","o":"ᴏ","p":"ᴘ","q":"ǫ","r":"ʀ","s":"s","t":"ᴛ",
        "u":"ᴜ","v":"ᴠ","w":"ᴡ","x":"x","y":"ʏ","z":"ᴢ",
        "A":"ᴀ","B":"ʙ","C":"ᴄ","D":"ᴅ","E":"ᴇ","F":"ꜰ","G":"ɢ","H":"ʜ","I":"ɪ","J":"ᴊ",
        "K":"ᴋ","L":"ʟ","M":"ᴍ","N":"ɴ","O":"ᴏ","P":"ᴘ","Q":"ǫ","R":"ʀ","S":"s","T":"ᴛ",
        "U":"ᴜ","V":"ᴠ","W":"ᴡ","X":"x","Y":"ʏ","Z":"ᴢ"
    }
    return "".join(mapping.get(c, c) for c in text)


# ─────────────────────────────
# 📥 USER JOINED VC (EVENT)
# ─────────────────────────────
@pytgcalls_client.on_participant_joined()
async def on_user_joined(_, update: Update):
    try:
        chat_id = update.chat_id
        user_id = update.participant.user_id if hasattr(update.participant, 'user_id') else update.participant.id
        
        user = await app.get_users(user_id)
        first_name = user.first_name or "ᴜsᴇʀ"

        # Ekdum simple aur short template
        text = (
            "<b>┃ 📥 ᴠᴄ ᴊᴏɪɴ ᴀʟᴇʀᴛ</b>\n\n"
            f"❯ {user.mention} ʜᴀs ᴊᴏɪɴᴇᴅ ᴛʜᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ! 🎉\n"
            f"🎯 <b>ɴᴀᴍᴇ:</b> {to_small_caps(first_name)}"
        )
        
        try:
            await app.send_message(chat_id, text)
        except Exception:
            pass 

    except Exception as e:
        LOGGER.error(f"[vc_join_error] {e}")


# ─────────────────────────────
# 📤 USER LEFT VC (EVENT)
# ─────────────────────────────
@pytgcalls_client.on_participant_left()
async def on_user_left(_, update: Update):
    try:
        chat_id = update.chat_id
        user_id = update.participant.user_id if hasattr(update.participant, 'user_id') else update.participant.id
        
        user = await app.get_users(user_id)
        first_name = user.first_name or "ᴜsᴇʀ"

        # Ekdum simple aur short template
        text = (
            "<b>┃ 📤 ᴠᴄ ʟᴇᴀᴠᴇ ᴀʟᴇʀᴛ</b>\n\n"
            f"❯ {user.mention} ʜᴀs ʟᴇғᴛ ᴛʜᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ. 🕊️\n"
            f"🎯 <b>ɴᴀᴍᴇ:</b> {to_small_caps(first_name)}"
        )
        
        try:
            await app.send_message(chat_id, text)
        except Exception:
            pass

    except Exception as e:
        LOGGER.error(f"[vc_leave_error] {e}")
