from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from utils import FAQ_KEYS

BUTTONS_PER_PAGE = 6  # например, 6 кнопок на страницу

def build_faq_keyboard(page: int) -> InlineKeyboardMarkup:
    keyboard = []
    start = page * BUTTONS_PER_PAGE
    end = min(start + BUTTONS_PER_PAGE, len(FAQ_KEYS))
    row = []

    for key in FAQ_KEYS[start:end]:
        row.append(InlineKeyboardButton(key.capitalize(), callback_data=f"faq_{key}"))
        if len(row) == 2:  # по 2 кнопки в строке
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)

    nav_buttons = []
    if page > 0:
        nav_buttons.append(InlineKeyboardButton("◀️ Назад", callback_data=f"page_{page - 1}"))
    if end < len(FAQ_KEYS):
        nav_buttons.append(InlineKeyboardButton("Вперёд ▶️", callback_data=f"page_{page + 1}"))
    if nav_buttons:
        keyboard.append(nav_buttons)

    return InlineKeyboardMarkup(keyboard)

