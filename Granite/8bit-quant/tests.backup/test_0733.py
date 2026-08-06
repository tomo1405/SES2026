import re
import string
from nltk.stem import PorterStemmer
from collections import Counter
from src_0733 import task_func
STEMMER = PorterStemmer()

def test_task_func():
    content = "This is a test sentence."
    expected_output = {'this': 1, 'is': 1, 'a': 1, 'test': 1, 'sentenc': 1}
    actual_output = task_func(content)
    assert actual_output == expected_output

def test_task_func_with_punctuation():
    content = "This, is a test! sentence."
    expected_output = {'this': 1, 'is': 1, 'a': 1, 'test': 1, 'sentenc': 1}
    actual_output = task_func(content)
    assert actual_output == expected_output

def test_task_func_with_multiple_sentences():
    content = "This is a test sentence. This is another test sentence."
    expected_output = {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'sentenc': 2}
    actual_output = task_func(content)
    assert actual_output == expected_output

def test_task_func_with_unicode_characters():
    content = "This is a test sentence with unicode characters like é, ñ, and ú."
    expected_output = {'this': 1, 'is': 1, 'a': 1, 'test': 1, 'sentenc': 1, 'e': 1, 'n': 1, 'u': 1}
    actual_output = task_func(content)
    assert actual_output == expected_output