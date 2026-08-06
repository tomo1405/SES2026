import pytest
from src_0521 import task_func

def test_task_func_empty_data():
    data = []
    expected_result = (dict(), None)
    assert task_func(data) == expected_result

def test_task_func_single_dict():
    data = [{"apple": 10, "banana": 5}]
    expected_result = ({'apple': 10, 'banana': 5}, None)
    assert task_func(data) == expected_result

def test_task_func_multiple_dicts():
    data = [{"apple": 10, "banana": 5}, {"apple": 15, "banana": 3, "orange": 8}]
    expected_result = ({'apple': 25, 'banana': 8, 'orange': 8}, None)
    assert task_func(data) == expected_result

def test_task_func_negative_value():
    data = [{"apple": -10, "banana": 5}]
    with pytest.raises(ValueError, match="Sales quantity must not be negative."):
        task_func(data)

def test_task_func_with_zero_values():
    data = [{"apple": 0, "banana": 0}, {"apple": 0, "banana": 0}]
    expected_result = ({'apple': 0, 'banana': 0}, None)
    assert task_func(data) == expected_result

def test_task_func_with_different_number_of_fruits():
    data = [{"apple": 10}, {"banana": 5, "orange": 8}, {"grape": 12}]
    expected_result = ({'apple': 10, 'banana': 5, 'orange': 8, 'grape': 12}, None)
    assert task_func(data) == expected_result