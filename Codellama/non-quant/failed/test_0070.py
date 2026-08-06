import pytest
from src_0070 import task_func

def test_task_func():
    # Test case 1: Test that the function returns a valid matplotlib figure
    fig = task_func({'EMPXX1': 10, 'EMPXX2': 20})
    assert isinstance(fig, matplotlib.figure.Figure)

    # Test case 2: Test that the function generates a histogram with the correct number of bins
    assert len(fig.axes[0].patches) == 10

    # Test case 3: Test that the function generates a histogram with the correct x-axis label
    assert fig.axes[0].get_xlabel() == 'Salary'

    # Test case 4: Test that the function generates a histogram with the correct y-axis label
    assert fig.axes[0].get_ylabel() == 'Number of Employees'

    # Test case 5: Test that the function generates a histogram with the correct title
    assert fig.axes[0].get_title() == 'Salary Distribution in EMPXX Department'

    # Test case 6: Test that the function generates a histogram with the correct x-axis range
    assert fig.axes[0].get_xlim() == (20000, 100000)

    # Test case 7: Test that the function generates a histogram with the correct y-axis range
    assert fig.axes[0].get_ylim() == (0, 100)

    # Test case 8: Test that the function generates a histogram with the correct number of employees
    assert len(fig.axes[0].patches[0].get_children()) == 10

    # Test case 9: Test that the function generates a histogram with the correct salary range
    assert fig.axes[0].patches[0].get_children()[0].get_height() == 100

    # Test case 10: Test that the function generates a histogram with the correct salary range
    assert fig.axes[0].patches[0].get_children()[0].get_width() == 10000