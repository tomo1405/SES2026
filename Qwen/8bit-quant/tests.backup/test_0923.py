import pytest
from src_0923 import task_func
import pandas as pd

def test_task_func_basic():
    data = [{'text': 'This is a test sentence.'}]
    column = 'text'
    expected_output = pd.DataFrame({'text': ['test sentence.']})
    assert task_func(data, column).equals(expected_output)

def test_task_func_empty_string():
    data = [{'text': ''}]
    column = 'text'
    expected_output = pd.DataFrame({'text': ['']})
    assert task_func(data, column).equals(expected_output)

def test_task_func_stopwords_only():
    data = [{'text': 'is a the'}]
    column = 'text'
    expected_output = pd.DataFrame({'text': ['']})
    assert task_func(data, column).equals(expected_output)

def test_task_func_punctuation():
    data = [{'text': 'Hello, world!'}]
    column = 'text'
    expected_output = pd.DataFrame({'text': ['Hello world']})
    assert task_func(data, column).equals(expected_output)

def test_task_func_numbers():
    data = [{'text': 'The year is 2023.'}]
    column = 'text'
    expected_output = pd.DataFrame({'text': ['year 2023']})
    assert task_func(data, column).equals(expected_output)

def test_task_func_multiple_rows():
    data = [
        {'text': 'This is a test sentence.'},
        {'text': 'Another example here.'}
    ]
    column = 'text'
    expected_output = pd.DataFrame({'text': ['test sentence.', 'example here.']})
    assert task_func(data, column).equals(expected_output)

def test_task_func_case_insensitivity():
    data = [{'text': 'IS A TEST SENTENCE.'}]
    column = 'text'
    expected_output = pd.DataFrame({'text': ['TEST SENTENCE']})
    assert task_func(data, column).equals(expected_output)