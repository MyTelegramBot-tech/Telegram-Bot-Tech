import os
from flask import Flask, request
import telebot
from handlers import *  # Импорт всех обработчиков

app = Flask(__name__)

# Получаем токен бота из переменной окружения
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise ValueError("Отсутствует TELEGRAM_BOT_TOKEN в переменных окружения")

bot = telebot.TeleBot(TOKEN)

@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'OK', 200

@app.route('/')
def index():
    return "Бот работает!", 200

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=f'https://your-app-name.onrender.com/{TOKEN}')  # Замените на настоящий адрес
    port = int(os.environ.get("PORT", 10000))  # Получаем порт от Render
    app.run(host="0.0.0.0", port=port)
