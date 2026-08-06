import re
from nltk.corpus import stopwords
from collections import Counter
from src_0850 import task_func

STOPWORDS = set(stopwords.words('english'))

def test_task_func():
    input_string = "This is a test\nThis is another test\nAnd this is yet another test"
    expected_output = {'This': 2, 'is': 2, 'a': 2, 'test': 3, 'another': 1, 'And': 1, 'yet': 1}
    actual_output = task_func(input_string)
    assert actual_output == expected_output

def test_task_func_with_empty_input():
    input_string = ""
    expected_output = {}
    actual_output = task_func(input_string)
    assert actual_output == expected_output

def test_task_func_with_one_word_per_line():
    input_string = "word1\nword2\nword3"
    expected_output = {'word1': 1, 'word2': 1, 'word3': 1}
    actual_output = task_func(input_string)
    assert actual_output == expected_output

def test_task_func_with_multiple_stopwords():
    input_string = "This is a test\nThis is another test\nAnd this is yet another test"
    expected_output = {'This': 2, 'is': 2, 'a': 2, 'test': 3, 'another': 1, 'And': 1, 'yet': 1}
    actual_output = task_func(input_string)
    assert actual_output == expected_output