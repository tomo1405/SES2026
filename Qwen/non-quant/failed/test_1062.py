import pytest
import numpy as np
from src_1062 import task_func

def test_task_func():
    # Create a sample input array
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # Call the function
    ax, normalized_data = task_func(arr)

    # Check if the output is a tuple with two elements
    assert isinstance(ax, plt.Axes)
    assert isinstance(normalized_data, np.ndarray)

    # Check if the shape of normalized_data is correct
    assert normalized_data.shape == (arr.shape[0],)

    # Check if the mean of normalized_data is approximately 0
    assert np.isclose(np.mean(normalized_data), 0, atol=1e-6)

    # Check if the standard deviation of normalized_data is approximately 1
    assert np.isclose(np.std(normalized_data), 1, atol=1e-6)

    # Check if the histogram plot is created correctly
    assert len(ax.patches) == 30  # Assuming 30 bins

    # Check if the PDF plot is created correctly
    assert len(ax.lines) == 1
    assert ax.lines[0].get_color() == 'r'
    assert ax.lines[0].get_linewidth() == 2

    # Check the title of the plot
    assert ax.get_title() == "Histogram of Normalized Data with Standard Normal PDF"

# Run the tests
if __name__ == "__main__":
    pytest.main()