from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Загружаем нейросети один раз при старте
classifier = pipeline("sentiment-analysis")
qa_model = pipeline("question-answering", model="deepset/roberta-base-squad2")

knowledge_base = """
Название проекта #1: Распознавание дорожных знаков системой YOLO. 
Детали: архитектура YOLOv7, датасет 5000 изображений.
Результат: точность mAP 0.92.
Авто проекта: Глеб.
Опыт работы: 3 года в аналитике данных.
Оценка: 10 баллов
"""

class UserRequest(BaseModel):
    text: str
    model_type: str


@app.post("/predict")
async def get_prediction(request: UserRequest):
    # Оценка тональности
    if request.model_type == "sentiment":
        prediction = classifier(request.text)[0]
        return {
        "original_text": request.text,
        "label": prediction['label'],
        "confidence": f"{prediction['score']:.2%}",
        "model_type": request.model_type,
        "status": "success"
    }
    # Количество слов
    elif request.model_type == "length":
        word_count = len(request.text.split())
        return {
            "original_text": request.text,
            "label": str(word_count),
            "confidence": "100%",
            "model_type": request.model_type,
            "status": "success"
        }
    # QA assistant
    elif request.model_type == "assistant":
        result = qa_model(question=request.text, context=knowledge_base)
        return {
            "original_text": request.text,
            "label": result["answer"],
            "confidence": f"{result['score']:.2%}",
            "model_type": request.model_type,
            "status": "success"
        }
    else:
        return {
            "message": "Unknown model type",
            "status": "error"
        }
