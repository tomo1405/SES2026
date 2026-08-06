import re
import string
from src_0825 import task_func

def test_task_func():
    text = "This is a sample text."
    num_words, num_punctuation = task_func(text)
    assert num_words == 4
    assert num_punctuation == 2

def test_task_func_with_punctuation():
    text = "This, is a sample! text."
    num_words, num_punctuation = task_func(text)
    assert num_words == 4
    assert num_punctuation == 4

def test_task_func_with_no_text():
    text = ""
    num_words, num_punctuation = task_func(text)
    assert num_words == 0
    assert num_punctuation == 0