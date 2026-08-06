import re
import string
from src_0825 import task_func

def test_task_func():
    text = "This is a test sentence. It contains words, punctuation marks, and numbers."
    num_words, num_punctuation = task_func(text)
    assert num_words == 6
    assert num_punctuation == 4

def test_task_func_with_numbers():
    text = "1234567890"
    num_words, num_punctuation = task_func(text)
    assert num_words == 1
    assert num_punctuation == 0

def test_task_func_with_punctuation():
    text = ".,:;?!-"
    num_words, num_punctuation = task_func(text)
    assert num_words == 0
    assert num_punctuation == 5