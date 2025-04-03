# config.py
import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

TOKEN = os.getenv('TOKEN')  # Получаем токен из переменной окружения
