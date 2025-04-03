from dotenv import load_dotenv
import os
import telebot

load_dotenv()  # Загружаем переменные из .env

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')  # Получаем токен из .env
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я ваш бот!")

bot.polling()
