import pytest
from src_0232 import task_func, ValueObject

def test_task_func_with_empty_list():
    ax = task_func([])
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Fit results: mu = 0.00,  std = 0.00"

def test_task_func_with_single_value_object():
    obj = ValueObject(mu=5, std=2)
    ax = task_func([obj])
    assert isinstance(ax, plt.Axes)
    assert ax.get_title().startswith("Fit results: mu = 5.00")

def test_task_func_with_multiple_value_objects():
    obj1 = ValueObject(mu=3, std=1)
    obj2 = ValueObject(mu=4, std=2)
    obj3 = ValueObject(mu=5, std=3)
    ax = task_func([obj1, obj2, obj3])
    assert isinstance(ax, plt.Axes)
    assert ax.get_title().startswith("Fit results: mu = ")

def test_task_func_with_large_number_of_objects():
    obj_list = [ValueObject(mu=i, std=i+1) for i in range(100)]
    ax = task_func(obj_list)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title().startswith("Fit results: mu = ")