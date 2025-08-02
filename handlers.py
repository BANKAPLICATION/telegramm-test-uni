import json

with open("faq.json", "r", encoding="utf-8") as f:
    FAQ = json.load(f)

def get_answer(user_text: str) -> str:
    text = user_text.lower()
    for key in FAQ:
        if key in text:
            return FAQ[key]
    return "Ваш вопрос передан сотруднику. Пожалуйста, ожидайте ответа."
