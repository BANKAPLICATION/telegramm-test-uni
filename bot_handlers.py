from telegram import Update
from telegram.ext import CallbackContext
from keyboard import build_faq_keyboard
from utils import get_answer, get_faq_answer_by_key

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Выберите вопрос:",
        reply_markup=build_faq_keyboard(0)
    )

def handle_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    query.answer()

    if data.startswith("faq_"):
        key = data[4:]
        answer = get_faq_answer_by_key(key)
        query.edit_message_text(f"**{key.capitalize()}**\n\n{answer}", parse_mode="Markdown")
    elif data.startswith("page_"):
        page = int(data.split("_")[1])
        query.edit_message_reply_markup(reply_markup=build_faq_keyboard(page))

def handle_message(update: Update, context: CallbackContext):
    user_text = update.message.text
    reply = get_answer(user_text)
    update.message.reply_text(reply)
