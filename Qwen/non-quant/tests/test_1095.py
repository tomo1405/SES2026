import pytest
from src_1095 import task_func
from collections import Counter

def test_task_func_no_dollar_words():
    text = "This is a test text without any dollar words."
    result = task_func(text)
    assert result == []

def test_task_func_single_dollar_word():
    text = "$word"
    result = task_func(text)
    assert result == [('word', 1)]

def test_task_func_multiple_dollar_words():
    text = "$word $word $anotherword"
    result = task_func(text)
    assert Counter(result) == Counter([('word', 2), ('anotherword', 1)])

def test_task_func_mixed_content():
    text = "This is a test with $word and $anotherword. Also $word!"
    result = task_func(text)
    assert Counter(result) == Counter([('word', 2), ('anotherword', 1)])

def test_task_func_empty_string():
    text = ""
    result = task_func(text)
    assert result == []

def test_task_func_only_dollar_signs():
    text = "$$$$"
    result = task_func(text)
    assert result == []

def test_task_func_special_characters():
    text = "$word! $word? $word."
    result = task_func(text)
    assert Counter(result) == Counter([('word', 3)])

def test_task_func_large_text():
    text = " ".join(["$word"] * 10 + ["$anotherword"] * 5 + ["$thirdword"] * 3)
    result = task_func(text)
    assert Counter(result) == Counter([('word', 10), ('anotherword', 5), ('thirdword', 3)])