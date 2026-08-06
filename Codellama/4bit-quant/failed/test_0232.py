import pytest
from src_0232 import task_func

def test_task_func_empty_list():
    obj_list = []
    ax = task_func(obj_list)
    assert ax.get_title() == "Fit results: mu = 0.00, std = 1.00"
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_xlim() == (0, 1)
    assert ax.get_ylim() == (0, 1)

def test_task_func_non_empty_list():
    obj_list = [ValueObject(mu=1, std=2), ValueObject(mu=3, std=4)]
    ax = task_func(obj_list)
    assert ax.get_title() == "Fit results: mu = 2.00, std = 2.00"
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_xlim() == (0, 1)
    assert ax.get_ylim() == (0, 1)

def test_task_func_invalid_input():
    obj_list = [ValueObject(mu=1, std=2), ValueObject(mu=3, std=4)]
    with pytest.raises(ValueError):
        task_func(obj_list, bins=0)