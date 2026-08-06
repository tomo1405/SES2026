import re
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from src_0728 import task_func

# Constants
SENTENCES = ['This is a sentence', 'Another sentence here', 'More sentences']

def test_task_func():
    s = 'This is a test sentence'
    expected_result = np.array([[1, 1, 1, 1, 0, 0, 0, 0, 0, 0]])
    result = task_func(s)
    assert np.array_equal(result, expected_result)

def test_task_func_with_multiple_words():
    s = 'This is a test sentence with multiple words'
    expected_result = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 0]])
    result = task_func(s)
    assert np.array_equal(result, expected_result)

def test_task_func_with_punctuation():
    s = 'This is a test! sentence with punctuation.'
    expected_result = np.array([[1, 1, 1, 1, 0, 0, 0, 0, 0, 0]])
    result = task_func(s)
    assert np.array_equal(result, expected_result)

def test_task_func_with_special_characters():
    s = 'This is a test$ sentence with special# characters.'
    expected_result = np.array([[1, 1, 1, 1, 0, 0, 0, 0, 0, 0]])
    result = task_func(s)
    assert np.array_equal(result, expected_result)

def test_task_func_with_empty_string():
    s = ''
    expected_result = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    result = task_func(s)
    assert np.array_equal(result, expected_result)

def test_task_func_with_whitespace_string():
    s = '    '
    expected_result = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    result = task_func(s)
    assert np.array_equal(result, expected_result)