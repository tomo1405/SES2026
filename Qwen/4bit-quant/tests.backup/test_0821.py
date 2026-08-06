import pytest
from src_0821 import task_func

def test_task_func_with_zero_words():
    result = task_func(0, 5)
    assert result == []

def test_task_func_with_zero_word_length():
    result = task_func(5, 0)
    assert result == ['', '', '', '', '']

def test_task_func_with_positive_values():
    result = task_func(3, 4)
    expected = ['dcVx', 'pXvT', 'rJzQ']
    assert result == expected

def test_task_func_with_large_word_length():
    result = task_func(1, 10)
    expected = ['bKxJzIaMnR']
    assert result == expected

def test_task_func_with_negative_num_words():
    with pytest.raises(ValueError):
        task_func(-1, 5)

def test_task_func_with_negative_word_length():
    with pytest.raises(ValueError):
        task_func(5, -1)

def test_task_func_with_large_num_words():
    result = task_func(10, 2)
    expected = ['xP', 'Yl', 'qG', 'uA', 'oK', 'tL', 'hW', 'sZ', 'jE', 'fR']
    assert result == expected