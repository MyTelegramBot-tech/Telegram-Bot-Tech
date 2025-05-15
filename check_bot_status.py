import requests
import os
from dotenv import load_dotenv

# Загружаем .env переменные
load_dotenv()

# Получаем данные из переменных окружения
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
MONITOR_BOT_TOKEN = os.getenv('MONITOR_BOT_TOKEN')
CHAT_ID = os.getenv('ALERT_CHAT_ID')

def check_bot():
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getMe'
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print("✅ Бот работает!")
        else:
            notify(f"❌ Бот не отвечает! Код {response.status_code}")
    except Exception as e:
        notify(f"❌ Ошибка при проверке бота:\n{e}")

def notify(message):
    notif_url = f'https://api.telegram.org/bot{MONITOR_BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    requests.post(notif_url, data=payload)

if __name__ == '__main__':
    check_bot()

