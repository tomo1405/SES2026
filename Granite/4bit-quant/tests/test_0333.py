import re
from collections import Counter
from nltk.corpus import stopwords
from src_0333 import task_func

def test_task_func():
    text = "This is a test sentence."
    expected_output = {'This': 1, 'is': 1, 'a': 1, 'test': 1, 'sentence.': 1}
    actual_output = task_func(text)
    assert actual_output == expected_output

def test_task_func_with_stopwords():
    text = "This is a test sentence with stopwords."
    expected_output = {'This': 1, 'is': 1, 'test': 1, 'sentence': 1, 'with': 1, 'stopwords.': 1}
    actual_output = task_func(text)
    assert actual_output == expected_output

def test_task_func_with_punctuation():
    text = "This, is a test! sentence."
    expected_output = {'This': 1, 'is': 1, 'a': 1, 'test': 1, 'sentence.': 1}
    actual_output = task_func(text)
    assert actual_output == expected_output

def test_task_func_with_numbers():
    text = "This is a test 1 sentence."
    expected_output = {'This': 1, 'is': 1, 'a': 1, 'test': 1, '1': 1, 'sentence.': 1}
    actual_output = task_func(text)
    assert actual_output == expected_output