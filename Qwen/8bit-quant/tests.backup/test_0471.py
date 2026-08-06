import pytest
from src_0471 import task_func
import matplotlib.pyplot as plt
import io
import sys

def test_task_func():
    # Redirect stdout to capture any print statements
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Create a sample list
    sample_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

    # Call the function
    ax = task_func(sample_list)

    # Check if the axes object is created correctly
    assert isinstance(ax, plt.Axes)

    # Check if the plot has the correct title
    assert ax.get_title() == "Histogram of Values"

    # Check if the x-axis label is correct
    assert ax.get_xlabel() == "Value"

    # Check if the y-axis label is correct
    assert ax.get_ylabel() == "Frequency"

    # Restore stdout
    sys.stdout = sys.__stdout__

    # Check if there were no print statements
    assert captured_output.getvalue() == ""

# Run the test
if __name__ == "__main__":
    pytest.main([__file__])