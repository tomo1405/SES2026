import pytest
from src_0271 import task_func

def test_task_func():
    sentence = "This is a test sentence."
    expected_output = {'This': 1, 'is': 1, 'a': 1, 'test': 1, 'sentence.': 1}
    actual_output = task_func(sentence)
    assert actual_output == expected_output, "Task function output does not match expected output."

def test_task_func_with_empty_sentence():
    sentence = ""
    expected_output = {}
    actual_output = task_func(sentence)
    assert actual_output == expected_output, "Task function output does not match expected output."

def test_task_func_with_whitespace_sentence():
    sentence = "   "
    expected_output = {}
    actual_output = task_func(sentence)
    assert actual_output == expected_output, "Task function output does not match expected output."