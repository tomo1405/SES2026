import re
import string
from src_0868 import task_func

def test_task_func():
    text1 = "Hello, world!"
    text2 = "How are you?"
    expected_output = ("Hello world", "How are you")

    actual_output = task_func(text1, text2)

    assert actual_output == expected_output

def test_task_func_with_punctuation():
    text1 = "Hello, world!"
    text2 = "How're you?"
    expected_output = ("Hello world", "Howre you")

    actual_output = task_func(text1, text2)

    assert actual_output == expected_output

def test_task_func_with_empty_string():
    text1 = ""
    text2 = "How are you?"
    expected_output = ("", "How are you")

    actual_output = task_func(text1, text2)

    assert actual_output == expected_output

def test_task_func_with_only_punctuation():
    text1 = ".,?"
    text2 = "!?,."
    expected_output = ("", "")

    actual_output = task_func(text1, text2)

    assert actual_output == expected_output