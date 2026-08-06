import pytest
from src_0521 import task_func
import collections
import matplotlib.pyplot as plt

def test_task_func_empty_data():
    data = []
    expected_total_sales = {}
    expected_ax = None
    total_sales, ax = task_func(data)
    assert total_sales == expected_total_sales
    assert ax == expected_ax

def test_task_func_single_dict():
    data = [{"apple": 10}]
    expected_total_sales = {"apple": 10}
    total_sales, ax = task_func(data)
    assert total_sales == expected_total_sales
    assert isinstance(ax, plt.Axes)

def test_task_func_multiple_dicts():
    data = [{"apple": 10}, {"banana": 5}, {"apple": 3, "banana": 2}]
    expected_total_sales = {"apple": 13, "banana": 7}
    total_sales, ax = task_func(data)
    assert total_sales == expected_total_sales
    assert isinstance(ax, plt.Axes)

def test_task_func_negative_values():
    data = [{"apple": -10}]
    with pytest.raises(ValueError, match="Sales quantity must not be negative."):
        task_func(data)

def test_task_func_duplicate_keys():
    data = [{"apple": 10}, {"apple": 5}]
    expected_total_sales = {"apple": 15}
    total_sales, ax = task_func(data)
    assert total_sales == expected_total_sales
    assert isinstance(ax, plt.Axes)

def test_task_func_ordered_dict():
    data = [{"banana": 5}, {"apple": 10}]
    expected_total_sales = {"apple": 10, "banana": 5}
    total_sales, ax = task_func(data)
    assert total_sales == expected_total_sales
    assert isinstance(ax, plt.Axes)