"""
Thumbnail toggle management module
Handles toggling thumbnail display on/off for music streams
"""

from pyrogram.types import InlineKeyboardButton

# Dictionary to track thumbnail preference for each chat
# chat_id -> True (enabled) or False (disabled)
thumbnail_settings = {}


def is_thumbnail_enabled(chat_id: int) -> bool:
    """
    Check if thumbnail is enabled for a chat
    Default: True (enabled)
    """
    return thumbnail_settings.get(chat_id, True)


def toggle_thumbnail(chat_id: int) -> bool:
    """
    Toggle thumbnail setting for a chat
    Returns the new state (True = enabled, False = disabled)
    """
    current_state = is_thumbnail_enabled(chat_id)
    new_state = not current_state
    thumbnail_settings[chat_id] = new_state
    return new_state


def get_thumbnail_button(chat_id: int) -> InlineKeyboardButton:
    """
    Get the thumbnail toggle button with appropriate emoji based on current state
    """
    is_enabled = is_thumbnail_enabled(chat_id)
    button_text = "🖼️ Thumbnail" if is_enabled else "🖼️ No Thumbnail"
    
    return InlineKeyboardButton(
        text=button_text,
        callback_data=f"toggle_thumbnail|{chat_id}"
    )


def set_thumbnail_state(chat_id: int, enabled: bool):
    """
    Explicitly set thumbnail state for a chat
    """
    thumbnail_settings[chat_id] = enabled


def get_all_thumbnail_settings():
    """
    Get all thumbnail settings (for debugging/logging)
    """
    return thumbnail_settings.copy()
