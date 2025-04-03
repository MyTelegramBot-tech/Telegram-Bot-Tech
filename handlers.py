# handlers.py
import telebot

bot = telebot.TeleBot("7578950871:AAGfv2zmRr6x532S0H4zJ2h2k95c_PNKSB4")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я ваш бот!")
