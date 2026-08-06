import pytest
from src_0659 import task_func

def test_task_func():
    texts = ['This is a test sentence.', 'Another test sentence!']
    expected_result = pd.DataFrame([[1, 1, 1], [1, 1, 1]])
    result = task_func(texts)
    assert result.equals(expected_result)

def test_task_func_with_empty_text():
    texts = ['', 'Another test sentence!']
    expected_result = pd.DataFrame([[0, 0, 0], [1, 1, 1]])
    result = task_func(texts)
    assert result.equals(expected_result)

def test_task_func_with_no_text():
    texts = []
    expected_result = pd.DataFrame()
    result = task_func(texts)
    assert result.equals(expected_result)