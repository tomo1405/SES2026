import pandas as pd
from src_0055 import task_func


def test_task_func():
    text = "This is a test sentence. This is another test sentence."
    expected_output = pd.DataFrame({
        'this': [1, 1],
        'is': [1, 1],
        'a': [1, 1],
        'test': [1, 1],
        'sentence': [1, 1],
        'another': [1, 1]
    })
    actual_output = task_func(text)
    assert actual_output.equals(expected_output)

def test_task_func_empty_text():
    text = ""
    expected_output = pd.DataFrame()
    actual_output = task_func(text)
    assert actual_output.equals(expected_output)

def test_task_func_single_sentence():
    text = "This is a test sentence."
    expected_output = pd.DataFrame({
        'this': [1],
        'is': [1],
        'a': [1],
        'test': [1],
        'sentence': [1]
    })
    actual_output = task_func(text)
    assert actual_output.equals(expected_output)