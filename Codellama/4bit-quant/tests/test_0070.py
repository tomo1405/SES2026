import matplotlib
import matplotlib.pyplot as plt
import pytest
from src_0070 import task_func


def test_task_func():
    # Test that the function returns a matplotlib.axes.Axes object
    assert isinstance(task_func({'EMPXX1': 10, 'EMPXX2': 20}), matplotlib.axes.Axes)

    # Test that the function plots the histogram correctly
    plt.hist(emp_salaries, bins=10, alpha=0.5)
    plt.title('Salary Distribution in EMPXX Department')
    plt.xlabel('Salary')
    plt.ylabel('Number of Employees')
    assert plt.gca().get_title() == 'Salary Distribution in EMPXX Department'
    assert plt.gca().get_xlabel() == 'Salary'
    assert plt.gca().get_ylabel() == 'Number of Employees'
    assert plt.gca().get_xlim() == (20000, 100000)
    assert plt.gca().get_ylim() == (0, 100)

    # Test that the function handles invalid input correctly
    with pytest.raises(ValueError):
        task_func({'EMPXX1': -10})

    with pytest.raises(ValueError):
        task_func({'EMPXX1': 10, 'EMPXX2': -20})