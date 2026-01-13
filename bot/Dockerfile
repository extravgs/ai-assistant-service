# /bot/Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Копируем зависимости бота (httpx, aiogram и т.д.)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Копируем код бота
COPY bot.py .

# Запускаем бота напрямую через интерпретатор
CMD ["python", "bot.py"]
