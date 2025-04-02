import os
import telebot

# Получаем токен из переменных окружения
TOKEN = os.getenv("BOT_TOKEN")

# Проверяем, что токен существует, иначе выбрасываем ошибку
if TOKEN is None:
    raise ValueError("Токен не найден! Убедись, что переменная BOT_TOKEN установлена.")

# Инициализируем бота
bot = telebot.TeleBot(TOKEN)

# Пример обработчика для /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, я бот!")

# Запуск бота
bot.polling()
