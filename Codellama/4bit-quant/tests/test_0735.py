import pytest
from src_0735 import task_func

def test_task_func():
    content = "This is a sample sentence."
    expected_result = {"DT": 1, "VBZ": 1, "NN": 2, "IN": 1, "DT": 1}
    assert task_func(content) == expected_result

def test_task_func_empty_input():
    content = ""
    expected_result = {}
    assert task_func(content) == expected_result

def test_task_func_single_word():
    content = "word"
    expected_result = {"NN": 1}
    assert task_func(content) == expected_result

def test_task_func_multiple_words():
    content = "This is a sample sentence."
    expected_result = {"DT": 1, "VBZ": 1, "NN": 2, "IN": 1, "DT": 1}
    assert task_func(content) == expected_result

def test_task_func_with_punctuation():
    content = "This, is a sample sentence!"
    expected_result = {"DT": 1, "VBZ": 1, "NN": 2, "IN": 1, "DT": 1}
    assert task_func(content) == expected_result

def test_task_func_with_special_characters():
    content = "This is a sample sentence with special characters: @#$%^&*()_+-=[]{}|;:,./<>?"
    expected_result = {"DT": 1, "VBZ": 1, "NN": 2, "IN": 1, "DT": 1}
    assert task_func(content) == expected_result