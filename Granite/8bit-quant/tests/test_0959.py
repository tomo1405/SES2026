import pytest
import random
import re
from src_0959 import task_func

def test_task_func():
    text = "This is a sample text."
    seed = 123
    random.seed(seed)
    scrambled_text = task_func(text, seed)
    assert isinstance(scrambled_text, str)
    assert scrambled_text != text

def test_task_func_with_seed():
    text = "This is another sample text."
    seed = 456
    random.seed(seed)
    scrambled_text = task_func(text, seed)
    assert isinstance(scrambled_text, str)
    assert scrambled_text != text

def test_task_func_with_no_seed():
    text = "This is yet another sample text."
    scrambled_text = task_func(text)
    assert isinstance(scrambled_text, str)
    assert scrambled_text != text

def test_task_func_with_empty_string():
    text = ""
    scrambled_text = task_func(text)
    assert isinstance(scrambled_text, str)
    assert scrambled_text == ""

def test_task_func_with_non_string_input():
    with pytest.raises(TypeError):
        task_func(123)