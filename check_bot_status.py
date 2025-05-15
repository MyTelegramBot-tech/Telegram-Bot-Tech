import requests

# Токен системного бота (который будет отправлять уведомления)
MONITOR_BOT_TOKEN = '7755444138:AAGidsK28LFWnDxIgSW8KjnmOi9hOsxDRJw'

# Твой chat_id
CHAT_ID = '6894271949'

# Токен основного бота, за которым следим
TELEGRAM_BOT_TOKEN = '7578950871:AAGfv2zmRr6x532S0H4zJ2h2k95c_PNKSB4'

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

