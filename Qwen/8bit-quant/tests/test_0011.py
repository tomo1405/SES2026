import pytest
from src_0011 import task_func

def test_task_func_empty_input():
    with pytest.raises(statistics.StatisticsError):
        task_func([])

def test_task_func_single_element():
    result = task_func([['1']])
    assert isinstance(result, tuple)
    assert len(result) == 3
    assert all(isinstance(x, (int, float)) for x in result)

def test_task_func_multiple_elements():
    result = task_func([['1', '2'], ['3', '4']])
    assert isinstance(result, tuple)
    assert len(result) == 3
    assert all(isinstance(x, (int, float)) for x in result)

def test_task_func_large_numbers():
    result = task_func([['999999999'] * 10])
    assert isinstance(result, tuple)
    assert len(result) == 3
    assert all(isinstance(x, (int, float)) for x in result)

def test_task_func_zero_range():
    result = task_func([['1']], RANGE=0)
    assert isinstance(result, tuple)
    assert len(result) == 3
    assert all(isinstance(x, (int, float)) for x in result)

def test_task_func_negative_range():
    with pytest.raises(ValueError):
        task_func([['1']], RANGE=-1)