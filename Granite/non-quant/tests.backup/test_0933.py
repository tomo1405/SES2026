import pytest
from collections import Counter
import re
from src_0933 import task_func

def test_task_func():
    word = "Hello"
    expected_result = [("ll", 2)]
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

def test_task_func_multiple_characters():
    word = "python"
    expected_result = [("th", 1), ("ho", 1), ("py", 1), ("yt", 1), ("on", 1)]
    result = task_func(word)
    assert result == expected_result