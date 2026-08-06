import pytest
from src_0070 import task_func

def test_task_func():
    dict1 = {'EMPXX': 10}
    ax = task_func(dict1)
    assert ax is not None
    assert ax.get_title() == 'Salary Distribution in EMPXX Department'
    assert ax.get_xlabel() == 'Salary'
    assert ax.get_ylabel() == 'Number of Employees'

def test_task_func_with_invalid_input():
    dict1 = {'Invalid Prefix': 10}
    with pytest.raises(ValueError):
        task_func(dict1)