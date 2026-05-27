from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ButtonStyle
from Oneforall import app

# Define all help buttons
HELP_BUTTONS = [
    ("H_B_1", "hb1"),
    ("H_B_2", "hb2"),
    ("H_B_3", "hb3"),
    ("H_B_4", "hb4"),
    ("H_B_5", "hb5"),
    ("H_B_6", "hb6"),
    ("H_B_7", "hb7"),
    ("H_B_8", "hb8"),
    ("H_B_9", "hb9"),
    ("H_B_10", "hb10"),
    ("H_B_11", "hb11"),
    ("H_B_12", "hb12"),
    ("H_B_13", "hb13"),
    ("H_B_14", "hb14"),
    ("H_B_15", "hb15"),
    ("H_B_25", "hb16"),
    ("H_B_26", "hb17"),
    ("H_B_27", "hb18"),
    ("H_B_28", "hb19"),
    ("✨ ғsᴜʙ", "hb20"),
    ("🎮 ғᴜɴ ɢᴀᴍᴇ", "hb21"),
]


def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close")]
    second = [
        InlineKeyboardButton(
            text=_["BACK_PAGE"],
            callback_data=f"mbot_cb",
            style=ButtonStyle.PRIMARY,
        ),
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
            style=ButtonStyle.PRIMARY,
        ),
        InlineKeyboardButton(
            text=_["NEXT_PAGE"],
            callback_data=f"mbot_cb",
            style=ButtonStyle.PRIMARY,
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["H_B_1"],
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text=_["H_B_2"],
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text=_["H_B_3"],
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_4"],
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text=_["H_B_5"],
                    callback_data="help_callback hb5",
                ),
                InlineKeyboardButton(
                    text=_["H_B_6"],
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_7"],
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text=_["H_B_8"],
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text=_["H_B_9"],
                    callback_data="help_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_10"],
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text=_["H_B_11"],
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text=_["H_B_12"],
                    callback_data="help_callback hb12",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_13"],
                    callback_data="help_callback hb13",
                ),
                InlineKeyboardButton(
                    text=_["H_B_14"],
                    callback_data="help_callback hb14",
                ),
                InlineKeyboardButton(
                    text=_["H_B_15"],
                    callback_data="help_callback hb15",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_26"],
                    callback_data="help_callback hb17",
                ),
                InlineKeyboardButton(
                    text=_["H_B_25"],
                    callback_data="help_callback hb16",
                ),
                InlineKeyboardButton(
                    "🎮 ғᴜɴ ɢᴀᴍᴇ",
                    callback_data="help_callback hb21",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_27"],
                    callback_data="help_callback hb18",
                ),
                InlineKeyboardButton(
                    text=_["H_B_28"],
                    callback_data="help_callback hb19",
                ),
                InlineKeyboardButton(
                    "✨ ғsᴜʙ",
                    callback_data="help_callback hb20",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
    return buttons


def group_help_pagination(_, page: int = 0):
    """Create paginated help buttons for group (3x3 grid with pagination)"""
    buttons_per_page = 9
    total_buttons = len(HELP_BUTTONS)
    total_pages = (total_buttons + buttons_per_page - 1) // buttons_per_page
    
    # Ensure page is within bounds
    page = max(0, min(page, total_pages - 1))
    
    # Get buttons for current page
    start_idx = page * buttons_per_page
    end_idx = min(start_idx + buttons_per_page, total_buttons)
    page_buttons = HELP_BUTTONS[start_idx:end_idx]
    
    # Build 3x3 grid
    keyboard = []
    for i in range(0, len(page_buttons), 3):
        row = []
        for j in range(3):
            if i + j < len(page_buttons):
                label, callback = page_buttons[i + j]
                # Check if label is a translation key or plain text
                if label.startswith("H_B_") or label in ["✨ ғsᴜʙ", "🎮 ғᴜɴ ɢᴀᴍᴇ"]:
                    button_text = _[label] if label in _else label
                else:
                    button_text = label
                row.append(
                    InlineKeyboardButton(
                        text=button_text,
                        callback_data=f"help_callback {callback}",
                    )
                )
        keyboard.append(row)
    
    # Add pagination and close buttons
    nav_row = []
    
    if page > 0:
        nav_row.append(
            InlineKeyboardButton(
                text="⬅️ PREV",
                callback_data=f"group_help_page {page - 1}",
            )
        )
    
    nav_row.append(
        InlineKeyboardButton(
            text="❌ CLOSE",
            callback_data="close_help_group",
        )
    )
    
    if page < total_pages - 1:
        nav_row.append(
            InlineKeyboardButton(
                text="NEXT ➡️",
                callback_data=f"group_help_page {page + 1}",
            )
        )
    
    keyboard.append(nav_row)
    
    return InlineKeyboardMarkup(keyboard)
