import pytest
from src_0183 import task_func

def test_task_func():
    df = pd.DataFrame({'Title': ['How to train a model', 'What is the meaning of life'], 'Content': ['Train a model using scikit-learn', 'The meaning of life is to find your purpose']})
    expected_output = [0, 1]
    assert task_func(df) == expected_output

def test_task_func_empty_input():
    df = pd.DataFrame({'Title': [], 'Content': []})
    expected_output = []
    assert task_func(df) == expected_output

def test_task_func_no_matching_titles():
    df = pd.DataFrame({'Title': ['This is a test', 'This is another test'], 'Content': ['This is a test', 'This is another test']})
    expected_output = []
    assert task_func(df) == expected_output