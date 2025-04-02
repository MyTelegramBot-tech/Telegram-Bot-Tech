import telebot
import os

TOKEN = os.getenv("TOKEN")  # Получаем токен из переменной окружения
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я работаю на Render!")

bot.polling()
