import pytest
from src_0938 import task_func
from collections import Counter
import re

def test_task_func():
    input_str = "Hello, World! 123"
    cleaned_str = re.sub('[^A-Za-z0-9]+', '', input_str).lower()
    freq_dict = Counter(cleaned_str)
    expected_output = Counter(dict(zip(cleaned_str, [1] * len(cleaned_str))))
    assert task_func(input_str) == expected_output

def test_task_func_empty_string():
    input_str = ""
    cleaned_str = re.sub('[^A-Za-z0-9]+', '', input_str).lower()
    freq_dict = Counter(cleaned_str)
    expected_output = Counter({})
    assert task_func(input_str) == expected_output

def test_task_func_with_special_characters():
    input_str = "Hello!@# World$%&"
    cleaned_str = re.sub('[^A-Za-z0-9]+', '', input_str).lower()
    freq_dict = Counter(cleaned_str)
    expected_output = Counter(dict(zip(cleaned_str, [1] * len(cleaned_str))))
    assert task_func(input_str) == expected_output