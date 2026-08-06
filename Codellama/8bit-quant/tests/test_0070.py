import matplotlib
import pytest
from src_0070 import task_func


def test_task_func():
    # Test case 1: Test that the function returns a valid matplotlib axis object
    dict1 = {'EMPXX1': 10, 'EMPXX2': 20, 'EMPXX3': 30}
    ax = task_func(dict1)
    assert isinstance(ax, matplotlib.axes.Axes)

    # Test case 2: Test that the function plots the correct histogram
    assert ax.get_title() == 'Salary Distribution in EMPXX Department'
    assert ax.get_xlabel() == 'Salary'
    assert ax.get_ylabel() == 'Number of Employees'
    assert ax.get_xlim() == (20000, 100000)
    assert ax.get_ylim() == (0, 100)

    # Test case 3: Test that the function handles invalid input correctly
    with pytest.raises(ValueError):
        task_func({'EMPXX1': 10, 'EMPXX2': 20, 'EMPXX3': 30, 'EMPXX4': 40})