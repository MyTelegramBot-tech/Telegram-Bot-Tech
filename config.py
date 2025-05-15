from dotenv import load_dotenv
import os
import telebot

load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')  # если используешь вебхук

bot = telebot.TeleBot(TOKEN)
