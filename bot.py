import asyncio
import httpx
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

TOKEN_STR = "YOUR_TOKEN_BOT_FATHER_TG"
FASTAPI_URL = "http://127.0.0.1:8000/predict"

bot = Bot(token=TOKEN_STR)
dp = Dispatcher()

user_modes = {}

def get_main_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="🧠 Ассистент (QA)")
    builder.button(text="🎭 Анализ тональности")
    builder.button(text="📊 Длина текста")
    builder.adjust(2)  # 2 кнопки в ряд
    return builder.as_markup(resize_keyboard=True)


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user_modes[message.from_user.id] = "assistant"  # Режим по умолчанию
    await message.answer(
        "Выберите режим работы с помощью кнопок ниже:",
        reply_markup=get_main_keyboard()
    )


@dp.message(F.text.in_(["🧠 Ассистент (QA)", "🎭 Анализ тональности", "📊 Длина текста"]))
async def set_mode(message: types.Message):
    if message.text == "🧠 Ассистент (QA)":
        user_modes[message.from_user.id] = "assistant"
        await message.answer("Переключено в режим Ассистента. Задавайте вопросы по проектам!")
    elif message.text == "🎭 Анализ тональности":
        user_modes[message.from_user.id] = "sentiment"
        await message.answer("Режим анализа тональности. Пришлите текст, и я скажу, добрый он или злой.")
    elif message.text == "📊 Длина текста":
        user_modes[message.from_user.id] = "length"
        await message.answer("Режим подсчета слов включен.")


@dp.message(F.text)
async def handle_message(message: types.Message):
    current_mode = user_modes.get(message.from_user.id, "assistant")

    payload = {
        "text": message.text,
        "model_type": current_mode
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(FASTAPI_URL, json=payload, timeout=15.0)
            data = response.json()

            if data.get("status") == "success":
                if current_mode == "sentiment":
                    answer = f"🎭 Тональность: {data['label']}\n🎯 Уверенность: {data['confidence']}"
                elif current_mode == "assistant":
                    answer = f"🤖 Ответ: {data['label']}"
                else:
                    answer = f"📊 Результат: {data['label']}"
            else:
                answer = "❌ Ошибка на стороне сервера."
        except Exception as e:
            answer = f"🔌 Ошибка связи: {e}"

    await message.answer(answer, reply_markup=get_main_keyboard())


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
