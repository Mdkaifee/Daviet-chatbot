# chatbot/bot.py

from .knowledge_base import find_answer

def get_bot_response(user_message):
    return find_answer(user_message)
