import re
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from src_0728 import task_func

# Constants
SENTENCES = ['This is a sentence', 'Another sentence here', 'More sentences']

def test_task_func():
    s = 'This is a test sentence'
    expected_output = np.array([[1, 1, 1, 1, 0, 0, 0, 0, 0, 0]])
    actual_output = task_func(s)
    assert np.array_equal(actual_output, expected_output), "Output does not match expected output"

def test_task_func_with_multiple_sentences():
    s = 'This is another test sentence'
    expected_output = np.array([[1, 1, 1, 1, 1, 0, 0, 0, 0, 0]])
    actual_output = task_func(s)
    assert np.array_equal(actual_output, expected_output), "Output does not match expected output"

def test_task_func_with_special_characters():
    s = 'This!@# is a test$% sentence'
    expected_output = np.array([[1, 1, 1, 1, 0, 0, 0, 0, 0, 0]])
    actual_output = task_func(s)
    assert np.array_equal(actual_output, expected_output), "Output does not match expected output"