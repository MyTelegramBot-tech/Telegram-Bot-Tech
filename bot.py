from flask import Flask, request
import telebot

app = Flask(__name__)

# Получаем токен из переменной окружения
TOKEN = '7578950871:AAGfv2zmRr6x532S0H4zJ2h2k95c_PNKSB4'  # замените на ваш реальный токен
bot = telebot.TeleBot(TOKEN)

# Добавляем маршрут для главной страницы
@app.route('/')
def index():
    return 'Bot is running!'  # Пожелание или простое сообщение

# Вебхук для бота
@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '!', 200

if __name__ == '__main__':
    # Удаляем старые вебхуки и устанавливаем новый
    bot.remove_webhook()
    bot.set_webhook(url='https://your-app-name.onrender.com/' + TOKEN)  # замените на ваш URL
    app.run(host="0.0.0.0", port=10000)  # используем порт 10000 для Render
