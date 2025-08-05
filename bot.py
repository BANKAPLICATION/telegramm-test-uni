from flask import Flask, request
from telegram import Bot, Update, ReplyKeyboardMarkup
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
from config import BOT_TOKEN
from handlers import get_answer

app = Flask(__name__)

bot = Bot(token=BOT_TOKEN)
dispatcher = Dispatcher(bot, None, workers=0, use_context=True)

# Главное меню
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

# Регистрируем handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# Входящие запросы от Telegram (webhook)
@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok", 200

@app.route("/", methods=["GET"])
def index():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
