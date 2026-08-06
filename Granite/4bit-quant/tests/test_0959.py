import pytest
from src_0959 import task_func
import random
import re

def test_task_func():
    text = "This is a sample text."
    seed = 42
    random.seed(seed)
    expected_output = "hsi sna elpmas."
    actual_output = task_func(text, seed)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_without_seed():
    text = "This is another sample text."
    expected_output = "hsi snaelpam te."
    actual_output = task_func(text)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_empty_string():
    text = ""
    expected_output = ""
    actual_output = task_func(text)
    assert actual_output == expected_output, "Output does not match expected output"