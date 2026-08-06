import re
import string
from src_0868 import task_func
import pytest

def test_task_func():
    text1 = "Hello, world!"
    text2 = "How are you?"
    expected_output = ("Hello world", "How are you")

    actual_output = task_func(text1, text2)

    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_punctuation():
    text1 = "Hello, world!"
    text2 = "How're you?"
    expected_output = ("Hello world", "Howre you")

    actual_output = task_func(text1, text2)

    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_empty_strings():
    text1 = ""
    text2 = ""
    expected_output = ("", "")

    actual_output = task_func(text1, text2)

    assert actual_output == expected_output, "Output does not match expected output"