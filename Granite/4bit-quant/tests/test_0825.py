import re
import string
from src_0825 import task_func

def test_task_func():
    text = "This is a test."
    word_count, punctuation_count = task_func(text)
    assert word_count == 4
    assert punctuation_count == 3

def test_task_func_with_punctuation():
    text = "This, is a test!"
    word_count, punctuation_count = task_func(text)
    assert word_count == 4
    assert punctuation_count == 4

def test_task_func_with_no_punctuation():
    text = "This is a test"
    word_count, punctuation_count = task_func(text)
    assert word_count == 4
    assert punctuation_count == 0

def test_task_func_with_empty_string():
    text = ""
    word_count, punctuation_count = task_func(text)
    assert word_count == 0
    assert punctuation_count == 0