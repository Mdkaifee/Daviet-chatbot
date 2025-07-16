# tests/test_bot.py

import pytest
from chatbot.bot import get_bot_response

def test_known_query():
    assert "DAVIET" in get_bot_response("Tell me about college")

def test_unknown_query():
    assert "couldn't find" in get_bot_response("What is the dress code?")

def test_hostel_query():
    assert "hostel" in get_bot_response("Tell me about the hostel")
