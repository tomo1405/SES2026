import pytest
from src_0523 import task_func
import matplotlib.pyplot as plt

def test_task_func_with_empty_data():
    assert task_func([]) is None

def test_task_func_with_single_dictionary():
    data = [{"Alice": 85}]
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_multiple_dictionaries():
    data = [{"Alice": 85}, {"Bob": 90}, {"Alice": 78}]
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_none_values():
    data = [{"Alice": None}, {"Bob": 90}]
    with pytest.raises(ValueError):
        task_func(data)

def test_task_func_with_negative_values():
    data = [{"Alice": -10}, {"Bob": 90}]
    with pytest.raises(ValueError):
        task_func(data)

def test_task_func_with_non_unique_keys():
    data = [{"Alice": 85}, {"Alice": 90}]
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_different_number_of_entries():
    data = [{"Alice": 85, "Bob": 90}, {"Alice": 78}]
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_ordered_output():
    data = [{"Alice": 85}, {"Bob": 90}, {"Charlie": 78}]
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)