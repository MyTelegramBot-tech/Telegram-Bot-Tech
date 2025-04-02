from flask import Flask, request
import telebot

app = Flask(__name__)

# Получаем токен из переменной окружения
TOKEN = '7578950871:AAGfv2zmRr6x532S0H4zJ2h2k95c_PNKSB4'
bot = telebot.TeleBot(TOKEN)

@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '!', 200

if __name__ == '__main__':
    # Удаляем старые вебхуки и устанавливаем новый
    bot.remove_webhook()
    bot.set_webhook(url='https://your-app-name.onrender.com/' + TOKEN)
    app.run(host="0.0.0.0", port=10000)  # Используем порт 10000, чтобы работал на Render

