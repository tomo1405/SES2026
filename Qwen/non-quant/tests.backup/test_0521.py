import pytest
from src_0521 import task_func
import collections
import matplotlib.pyplot as plt

def test_task_func_empty_data():
    data = []
    expected_total_sales = {}
    expected_ax = None
    assert task_func(data) == (expected_total_sales, expected_ax)

def test_task_func_single_dict():
    data = [{'apple': 10, 'banana': 5}]
    expected_total_sales = {'apple': 10, 'banana': 5}
    total_sales, ax = task_func(data)
    assert total_sales == expected_total_sales
    assert isinstance(ax, plt.BarContainer)

def test_task_func_multiple_dicts():
    data = [{'apple': 10, 'banana': 5}, {'apple': 5, 'orange': 8}]
    expected_total_sales = {'apple': 15, 'banana': 5, 'orange': 8}
    total_sales, ax = task_func(data)
    assert total_sales == expected_total_sales
    assert isinstance(ax, plt.BarContainer)

def test_task_func_negative_value():
    data = [{'apple': -10, 'banana': 5}]
    with pytest.raises(ValueError) as excinfo:
        task_func(data)
    assert str(excinfo.value) == "Sales quantity must not be negative."

def test_task_func_duplicate_keys():
    data = [{'apple': 10, 'banana': 5}, {'apple': 5, 'banana': 3}]
    expected_total_sales = {'apple': 15, 'banana': 8}
    total_sales, ax = task_func(data)
    assert total_sales == expected_total_sales
    assert isinstance(ax, plt.BarContainer)

def test_task_func_ordered_dict():
    data = [{'banana': 5, 'apple': 10}, {'apple': 5, 'banana': 3}]
    expected_total_sales = {'apple': 15, 'banana': 8}
    total_sales, ax = task_func(data)
    assert total_sales == expected_total_sales
    assert isinstance(ax, plt.BarContainer)