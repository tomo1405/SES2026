import pytest
from src_0521 import task_func


def test_task_func_empty_data():
    data = []
    expected_total_sales = {}
    expected_ax = None

    total_sales, ax = task_func(data)

    assert total_sales == expected_total_sales
    assert ax == expected_ax


def test_task_func_single_data():
    data = [{"apple": 10, "banana": 20, "orange": 30}]
    expected_total_sales = {"apple": 10, "banana": 20, "orange": 30}
    expected_ax = None

    total_sales, ax = task_func(data)

    assert total_sales == expected_total_sales
    assert ax == expected_ax


def test_task_func_multiple_data():
    data = [{"apple": 10, "banana": 20, "orange": 30}, {"apple": 5, "banana": 10, "orange": 15}]
    expected_total_sales = {"apple": 15, "banana": 30, "orange": 45}
    expected_ax = None

    total_sales, ax = task_func(data)

    assert total_sales == expected_total_sales
    assert ax == expected_ax


def test_task_func_negative_sales():
    data = [{"apple": 10, "banana": 20, "orange": -30}]
    expected_total_sales = {}
    expected_ax = None

    with pytest.raises(ValueError):
        total_sales, ax = task_func(data)

    assert total_sales == expected_total_sales
    assert ax == expected_ax