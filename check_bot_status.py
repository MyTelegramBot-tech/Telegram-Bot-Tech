import requests
import os

# Токен и ID чата для уведомлений
MONITOR_BOT_TOKEN = 'ТОКЕН_ВАШЕГО_СИСТЕМНОГО_БОТА'
CHAT_ID = '1271362249'  # ваш chat_id

# Токен основного бота, которого мониторим
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')  # или вставь прямо

def check_bot():
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getMe'
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print("✅ Бот работает!")
        else:
            notify(f"❌ Бот не отвечает! Код {response.status_code}")
    except Exception as e:
        notify(f"❌ Ошибка при проверке бота: {e}")

def notify(message):
    notif_url = f'https://api.telegram.org/bot{MONITOR_BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    requests.post(notif_url, data=payload)

if __name__ == '__main__':
    check_bot()
