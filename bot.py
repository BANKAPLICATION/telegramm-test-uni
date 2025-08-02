from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import BOT_TOKEN
from handlers import get_answer

# Кнопки для главного меню
keyboard = [["Стоимость", "Документы"], ["Сроки", "Направления"]]
markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def start(update, context):
    update.message.reply_text(
        "Здравствуйте! Я помогу вам с поступлением.\nВыберите интересующий вас вопрос:",
        reply_markup=markup
    )

def handle_message(update, context):
    user_text = update.message.text
    reply = get_answer(user_text)
    update.message.reply_text(reply)

def main():
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
