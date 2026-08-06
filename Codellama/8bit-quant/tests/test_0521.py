import pytest
from src_0521 import task_func


def test_task_func_empty_data():
    data = []
    expected_result = (dict(), None)
    assert task_func(data) == expected_result


def test_task_func_invalid_data():
    data = [{"apple": 10, "banana": -5}]
    with pytest.raises(ValueError):
        task_func(data)


def test_task_func_valid_data():
    data = [{"apple": 10, "banana": 5}, {"apple": 5, "banana": 10}]
    expected_result = ({"apple": 15, "banana": 15}, <matplotlib.axes._subplots.AxesSubplot object at 0x7f8369000000>)
    assert task_func(data) == expected_result