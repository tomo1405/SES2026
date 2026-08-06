import pytest
from src_0214 import task_func
import time
import random
import matplotlib.pyplot as plt
from scipy.stats import kurtosis

def test_task_func():
    # Mock the time.sleep function to avoid actual sleeping
    original_sleep = time.sleep
    def mock_sleep(seconds):
        pass
    time.sleep = mock_sleep

    # Mock the random.random function to return predictable values
    original_random = random.random
    def mock_random():
        return 0.5
    random.random = mock_random

    # Capture stdout to check for the 'Interrupted by user' message
    import sys
    from io import StringIO
    captured_output = StringIO()
    sys.stdout = captured_output

    # Call the function with a small number of intervals
    ax, kurtosis_value = task_func(intervals=3, seed=0)

    # Restore the original functions and stdout
    time.sleep = original_sleep
    random.random = original_random
    sys.stdout = sys.__stdout__

    # Check the kurtosis value
    assert kurtosis_value == kurtosis([0.5, 0.5, 0.5], nan_policy='omit')

    # Check that the plot was created correctly
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 1
    assert len(ax.lines[0].get_xdata()) == 3
    assert len(ax.lines[0].get_ydata()) == 3
    assert all(y == 0.5 for y in ax.lines[0].get_ydata())

    # Check that no 'Interrupted by user' message was printed
    assert captured_output.getvalue() == ''

# Run the test
if __name__ == "__main__":
    pytest.main()