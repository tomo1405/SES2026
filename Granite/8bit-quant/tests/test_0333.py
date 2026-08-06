import pytest
from src_0333 import task_func

def test_task_func():
    text = "This is a sample text. It contains some words."
    expected_output = {'sample': 1, 'text.': 1, 'contains': 1, 'some': 1, 'words.': 1}
    actual_output = task_func(text)
    assert actual_output == expected_output

def test_task_func_empty_text():
    text = ""
    expected_output = {}
    actual_output = task_func(text)
    assert actual_output == expected_output

def test_task_func_only_stopwords():
    text = "This is a sample text. It contains some stopwords like 'the' and 'is'."
    expected_output = {'stopwords': 2, 'like': 1, 'the': 1, 'and': 1}
    actual_output = task_func(text)
    assert actual_output == expected_output