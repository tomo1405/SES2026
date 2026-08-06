import pytest
from src_0406 import task_func
import matplotlib.pyplot as plt

def test_task_func():
    points = 10
    y, ax = task_func(points)
    
    # Check that y is a list of the correct length
    assert isinstance(y, list)
    assert len(y) == points
    
    # Check that all elements in y are floats between 0 and 1
    for value in y:
        assert isinstance(value, float)
        assert 0 <= value <= 1
    
    # Check that ax is a matplotlib Axes object
    assert isinstance(ax, plt.Axes)

    # Since we cannot directly check the plot, we can at least ensure that the plot has been created
    assert ax.has_data()

    # Close the plot to prevent it from displaying during tests
    plt.close(ax.figure)