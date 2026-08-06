import pytest
from src_1064 import task_func
import numpy as np

def test_task_func():
    # Create a sample input array
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # Call the function
    ax = task_func(arr)

    # Check if the returned object is an AxesSubplot instance
    assert isinstance(ax, plt.Axes), "The function should return an AxesSubplot instance."

    # Check if the title is set correctly
    assert ax.get_title() == "Explained Variance Ratio of Principal Components", "The plot title is incorrect."

    # Check if the x-ticks and labels are set correctly
    xticks, xticklabels = ax.get_xticks(), ax.get_xticklabels()
    assert xticks == [0], "The x-ticks are incorrect."
    assert [label.get_text() for label in xticklabels] == ["PC1"], "The x-tick labels are incorrect."

    # Check if the bar plot has the correct data
    bars = ax.patches
    assert len(bars) == 1, "There should be exactly one bar in the plot."
    assert bars[0].get_height() == pytest.approx(0.9999999999999999, rel=1e-5), "The height of the bar is incorrect."

# Run the tests
if __name__ == "__main__":
    pytest.main()