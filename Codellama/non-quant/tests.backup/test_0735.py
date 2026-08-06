import pytest
from src_0735 import task_func

def test_task_func():
    content = "This is a sample sentence."
    expected_result = {"DT": 1, "VBZ": 1, "DT": 1, "NN": 1, "IN": 1, "DT": 1, "NN": 1, "." : 1}
    assert task_func(content) == expected_result

def test_task_func_empty_string():
    content = ""
    expected_result = {}
    assert task_func(content) == expected_result

def test_task_func_single_word():
    content = "word"
    expected_result = {"NN": 1}
    assert task_func(content) == expected_result

def test_task_func_multiple_words():
    content = "This is a sample sentence."
    expected_result = {"DT": 1, "VBZ": 1, "DT": 1, "NN": 1, "IN": 1, "DT": 1, "NN": 1, "." : 1}
    assert task_func(content) == expected_result

def test_task_func_with_punctuation():
    content = "This is a sample sentence!?"
    expected_result = {"DT": 1, "VBZ": 1, "DT": 1, "NN": 1, "IN": 1, "DT": 1, "NN": 1, "." : 1, "!" : 1, "?" : 1}
    assert task_func(content) == expected_result

def test_task_func_with_numbers():
    content = "This is a sample sentence with numbers 12345."
    expected_result = {"DT": 1, "VBZ": 1, "DT": 1, "NN": 1, "IN": 1, "DT": 1, "NN": 1, "." : 1, "CD" : 1}
    assert task_func(content) == expected_result