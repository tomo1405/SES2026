import pytest
from src_0070 import task_func

def test_task_func():
    dict1 = {'EMP001': 10, 'EMP002': 5, 'EMP003': 15}
    ax = task_func(dict1)
    assert ax is not None
    assert ax.get_title() == 'Salary Distribution in EMPXX Department'
    assert ax.get_xlabel() == 'Salary'
    assert ax.get_ylabel() == 'Number of Employees'