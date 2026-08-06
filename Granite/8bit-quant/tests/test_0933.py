import pytest
from collections import Counter
import re
from src_0933 import task_func

def test_task_func():
    word = "Hello World"
    expected_result = [("ll", 3)]
    result = task_func(word)
    assert result == expected_result

def test_task_func_empty_string():
    word = ""
    expected_result = []
    result = task_func(word)
    assert result == expected_result

def test_task_func_single_character():
    word = "a"
    expected_result = []
    result = task_func(word)
    assert result == expected_result