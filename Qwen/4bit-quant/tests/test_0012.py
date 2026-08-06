import pytest
from src_0012 import task_func

def test_task_func_with_empty_input():
    T1 = []
    result = task_func(T1)
    assert result == (0.0, 0.0, 0.0), "Test failed for empty input"

def test_task_func_with_single_element():
    T1 = [['1']]
    result = task_func(T1)
    assert isinstance(result, tuple) and len(result) == 3, "Test failed for single element input"

def test_task_func_with_multiple_elements():
    T1 = [['1', '2'], ['3', '4']]
    result = task_func(T1)
    assert isinstance(result, tuple) and len(result) == 3, "Test failed for multiple elements input"

def test_task_func_with_max_value_zero():
    T1 = [['1', '2'], ['3', '4']]
    with pytest.raises(ValueError):
        task_func(T1, max_value=0)

def test_task_func_with_large_numbers():
    T1 = [['1000', '2000'], ['3000', '4000']]
    result = task_func(T1)
    assert isinstance(result, tuple) and len(result) == 3, "Test failed for large numbers input"

def test_task_func_with_negative_numbers():
    T1 = [['-1', '-2'], ['-3', '-4']]
    with pytest.raises(ValueError):
        task_func(T1)

def test_task_func_with_non_integer_strings():
    T1 = [['a', 'b'], ['c', 'd']]
    with pytest.raises(ValueError):
        task_func(T1)