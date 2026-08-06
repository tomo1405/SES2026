import pytest
from src_0406 import task_func
import matplotlib.pyplot as plt
import io
import sys

def test_task_func():
    points = 10
    y, ax = task_func(points)
    
    # Check if y is a list of length 'points'
    assert isinstance(y, list), "y should be a list"
    assert len(y) == points, f"y should have {points} elements"

    # Check if all elements in y are between 0 and 1
    assert all(0 <= value <= 1 for value in y), "All values in y should be between 0 and 1"

    # Capture the plot output to check if it's created
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        plt.show()
    except Exception as e:
        assert False, f"Failed to display plot: {e}"
    finally:
        sys.stdout = old_stdout

    # Check if the axes object is correctly created
    assert isinstance(ax, plt.Axes), "ax should be an instance of matplotlib.axes.Axes"

# Run the tests
if __name__ == "__main__":
    pytest.main()