from pyrogram.types import InlineKeyboardButton

from pyrogram.enums import ButtonStyle

class BUTTONS(object):
    MBUTTON = [
        [
            InlineKeyboardButton("Hɪsᴛᴏʀʏ", callback_data="mplus HELP_History"),
        ],
        [
            InlineKeyboardButton("Tᴀɢ-Aʟʟ", callback_data="mplus HELP_TagAll"),
            InlineKeyboardButton("Iɴꜰᴏ", callback_data="mplus HELP_Info"),
            InlineKeyboardButton("Exᴛʀᴀ", callback_data="mplus HELP_Extra"),
        ],
        [
            InlineKeyboardButton("ᴄᴏᴜᴘʟᴇꜱ", callback_data="mplus HELP_Couples"),
            InlineKeyboardButton("Aᴄᴛɪᴏɴ", callback_data="mplus HELP_Action"),
            InlineKeyboardButton("Sᴇᴀʀᴄʜ", callback_data="mplus HELP_Search"),
        ],
        [
            InlineKeyboardButton("ғᴏɴᴛ", callback_data="mplus HELP_Font"),
            InlineKeyboardButton("Bᴏᴛs", callback_data="mplus HELP_Bots"),
            InlineKeyboardButton("Ⓣ-ɢʀᴀᴘʜ", callback_data="mplus HELP_TG"),
        ],
        [
            InlineKeyboardButton("Sᴏᴜʀᴄᴇ", callback_data="mplus HELP_Source"),
            InlineKeyboardButton("Tʀᴜᴛʜ-ᗪᴀʀᴇ", callback_data="mplus HELP_TD"),
            InlineKeyboardButton("Qᴜɪᴢ", callback_data="mplus HELP_Quiz"),
        ],
        [
            InlineKeyboardButton("ᴛᴛs", callback_data="mplus HELP_TTS"),
            InlineKeyboardButton("Rᴀᴅɪᴏ", callback_data="mplus HELP_Radio"),
            InlineKeyboardButton("ǫᴜᴏᴛʟʏ", callback_data="mplus HELP_Q"),
        ],
        [
            InlineKeyboardButton("ᴛʜᴜᴍʙ", callback_data="mplus HELP_Thumb", style=ButtonStyle.PRIMARY),
            InlineKeyboardButton("ᴀᴜᴛᴏᴘʟᴀʏ", callback_data="mplus HELP_Autoplay", style=ButtonStyle.PRIMARY),
        ],
        [
            InlineKeyboardButton("⬅️", callback_data="settings_back_helper", style=ButtonStyle.SUCCESS),
            InlineKeyboardButton("➡️", callback_data="managebot123 settings_back_helper", style=ButtonStyle.SUCCESS),
        ],
    ]
