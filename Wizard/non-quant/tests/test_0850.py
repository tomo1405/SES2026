python
import re
import pytest
from nltk.corpus import stopwords
from collections import Counter

STOPWORDS = set(stopwords.words('english'))

def task_func(input_string):
    lines = input_string.split('\n')
    word_count = Counter()
    for line in lines:
        words = re.findall(r'\b\w+\b', line)
        words = [word for word in words if word not in STOPWORDS]
        word_count.update(words)
    return dict(word_count)

def test_task_func():
    input_string = "This is a test string.\nIt contains some words."
    expected_output = {'test': 1, 'string': 1, 'contains': 1, 'some': 1, 'words': 1}
    assert task_func(input_string) == expected_output

def test_task_func_empty_string():
    input_string = ""
    expected_output = {}
    assert task_func(input_string) == expected_output

def test_task_func_single_word():
    input_string = "test"
    expected_output = {'test': 1}
    assert task_func(input_string) == expected_output

def test_task_func_single_word_with_stopword():
    input_string = "the"
    expected_output = {}
    assert task_func(input_string) == expected_output

def test_task_func_multiple_words_with_stopwords():
    input_string = "the quick brown fox jumps over the lazy dog"
    expected_output = {}
    assert task_func(input_string) == expected_output

def test_task_func_multiple_lines():
    input_string = "This is a test string.\nIt contains some words.\nHere is another line."
    expected_output = {'test': 1, 'string': 1, 'contains': 1, 'some': 1, 'words': 1, 'another': 1, 'line': 1}
    assert task_func(input_string) == expected_output

def test_task_func_multiple_lines_with_stopwords():
    input_string = "This is a test string.\nIt contains some words.\nHere is another line.\nThe quick brown fox jumps over the lazy dog"
    expected_output = {'test': 1, 'string': 1, 'contains': 1, 'some': 1, 'words': 1, 'another': 1, 'line': 1}
    assert task_func(input_string) == expected_output