# handlers.py
from bot import bot

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я ваш бот!")
