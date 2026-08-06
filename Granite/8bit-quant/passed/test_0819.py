import re
import string
from src_0819 import task_func
import pytest

PUNCTUATION = string.punctuation

def test_task_func():
    text = "Hello, world! How are you?"
    expected_output = ["hello", "world", "how", "are", "you"]
    actual_output = task_func(text)
    assert actual_output == expected_output

def test_task_func_with_punctuation():
    text = "Hello, world! How're you?"
    expected_output = ["hello", "world", "howre", "you"]
    actual_output = task_func(text)
    assert actual_output == expected_output

def test_task_func_with_numbers():
    text = "Hello, 123 world! How're you?"
    expected_output = ["hello", "123", "world", "howre", "you"]
    actual_output = task_func(text)
    assert actual_output == expected_output