import pytest
from src_0056 import task_func

def test_task_func():
    text = "This is a sample text. It has multiple sentences. Each sentence has multiple words."
    expected_output = pd.Series({"Sentence 1": 4, "Sentence 2": 5, "Sentence 3": 6})
    assert task_func(text).equals(expected_output)

def test_task_func_with_stopwords():
    text = "These are the words to ignore. This is a sample text. It has multiple sentences. Each sentence has multiple words."
    expected_output = pd.Series({"Sentence 1": 4, "Sentence 2": 5, "Sentence 3": 6})
    assert task_func(text).equals(expected_output)

def test_task_func_with_empty_string():
    text = ""
    expected_output = pd.Series()
    assert task_func(text).equals(expected_output)

def test_task_func_with_invalid_input():
    text = "This is a sample text. It has multiple sentences. Each sentence has multiple words."
    with pytest.raises(ValueError):
        task_func(text, invalid_input=True)