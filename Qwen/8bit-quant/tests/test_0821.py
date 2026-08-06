import pytest
from src_0821 import task_func

def test_task_func_negative_num_words():
    with pytest.raises(ValueError) as exc_info:
        task_func(-1, 5)
    assert str(exc_info.value) == "num_words and word_length must be non-negative"

def test_task_func_negative_word_length():
    with pytest.raises(ValueError) as exc_info:
        task_func(5, -1)
    assert str(exc_info.value) == "num_words and word_length must be non-negative"

def test_task_func_zero_num_words():
    result = task_func(0, 5)
    assert result == []

def test_task_func_zero_word_length():
    result = task_func(5, 0)
    assert result == ['', '', '', '', '']

def test_task_func_positive_values():
    result = task_func(3, 5)
    expected = ['aYzXq', 'aYzXq', 'aYzXq']
    assert result == expected

def test_task_func_reproducibility():
    result1 = task_func(3, 5)
    result2 = task_func(3, 5)
    assert result1 == result2