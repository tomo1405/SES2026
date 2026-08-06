import re
import string
from src_0819 import task_func
import pytest

def test_task_func():
    text = "Hello, world! How are you?"
    expected_output = ["hello", "world", "how", "are", "you"]
    actual_output = task_func(text)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_punctuation():
    text = "Hello, world! How're you?"
    expected_output = ["hello", "world", "howre", "you"]
    actual_output = task_func(text)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_numbers():
    text = "12345 67890"
    expected_output = ["12345", "67890"]
    actual_output = task_func(text)
    assert actual_output == expected_output, "Output does not match expected output"