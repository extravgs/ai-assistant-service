# Выбираем легкий образ
FROM python:3.10-slim

# Устанавливаем рабочую папку
WORKDIR /app

# Копируем только файл с библиотеками
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir torch==2.5.1 --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir -r requirements.txt

# Теперь копируем основной код сервера
COPY server.py .

# Указываем, какой порт будет использовать контейнер
EXPOSE 8000

# Запускаем FastAPI через uvicorn
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "800
