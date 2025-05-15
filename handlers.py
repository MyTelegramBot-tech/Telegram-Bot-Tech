# handlers.py
from config import bot  # ← импортируем ОДИН и тот же экземпляр

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я ваш бот!")
