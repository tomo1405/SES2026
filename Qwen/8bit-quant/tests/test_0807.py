from typing import Counter

from src_0807 import task_func


def test_task_func_basic():
    text = "This is a test sentence."
    expected_output = Counter([(('this', 'is'), 1), (('is', 'a'), 1), (('a', 'test'), 1), (('test', 'sentence'), 1)])
    assert task_func(text) == expected_output

def test_task_func_with_stopwords():
    text = "This is a test sentence with some stopwords."
    expected_output = Counter([(('this', 'test'), 1), (('test', 'sentence'), 1), (('sentence', 'stopwords'), 1)])
    assert task_func(text) == expected_output

def test_task_func_empty_string():
    text = ""
    expected_output = Counter()
    assert task_func(text) == expected_output

def test_task_func_single_word():
    text = "Hello"
    expected_output = Counter()
    assert task_func(text) == expected_output

def test_task_func_punctuation():
    text = "Hello, world!"
    expected_output = Counter([(('hello', 'world'), 1)])
    assert task_func(text) == expected_output

def test_task_func_n_value():
    text = "This is a test sentence."
    n = 3
    expected_output = Counter([(('this', 'is', 'a'), 1), (('is', 'a', 'test'), 1), (('a', 'test', 'sentence'), 1)])
    assert task_func(text, n=n) == expected_output

def test_task_func_case_insensitivity():
    text = "This is a TEST sentence."
    expected_output = Counter([(('this', 'is'), 1), (('is', 'a'), 1), (('a', 'test'), 1), (('test', 'sentence'), 1)])
    assert task_func(text) == expected_output