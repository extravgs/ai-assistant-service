# ai-assistant-service
![AIPOWER](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F2kk8xm3efonxlmajksm8.png)
=====================
**Multi-purpose AI Assistant: QA & Sentiment Analysis Service**
=====================
**Описание:**
=====================
Микросервисная система на базе Python, объединяющая возможности современных LLM-моделей (Transformers) и удобный интерфейс через Telegram-бота. 

Проект демонстрирует разделение логики на Backend (обработка ИИ) и Frontend (интерфейс пользователя).
***
**Ключевой функционал:**
=====================
AI Ассистент (RAG): Система ответов на вопросы по кастомной базе знаний (использована модель roberta-base-squad2).

Анализ тональности: Классификация эмоциональной окраски текста (модель sentiment-analysis).

Microservice Architecture: Backend на FastAPI взаимодействует с Telegram-ботом через асинхронные HTTP-запросы (httpx).

Интерактивный UI: Бот с использованием aiogram 3.x, поддерживающий систему состояний и кнопочное меню.

***
**Технологический стек:**
=====================
  Tools         | Name & Version
----------------|----------------------
Language:       | Python 3.10+
ML Frameworks:  | Hugging Face Transformers, PyTorch, sentiment-analysis, deepset/roberta-base-squad2
API Framework:  | FastAPI, Uvicorn, Pydantic
Bot API:        | Aiogram 3
***
**Как запустить:**
=====================
1. Клонировать репозиторий.
  
2. Установить зависимости:   ```**pip install -r requirements.txt.**```

3. В первом терминале запустить сервер:   ```**uvicorn server:app.**```

4. Во втором терминале запустить бота:   ```**python bot.py.**```

