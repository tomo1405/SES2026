import pytest
from src_0197 import task_func
import numpy as np
from matplotlib import pyplot as plt

def test_task_func():
    length = 10
    range_limit = 50
    seed = 42

    axes, random_numbers = task_func(length, range_limit, seed)

    # Check that the random numbers are within the specified range and sorted
    assert all(1 <= num <= range_limit for num in random_numbers), "Random numbers are out of range"
    assert random_numbers == sorted(random_numbers), "Random numbers are not sorted"

    # Check that the plot is created correctly
    assert isinstance(axes, plt.Axes), "The returned object is not a matplotlib Axes instance"

    # Check that the plot contains the correct number of bars
    bars = axes.patches
    assert len(bars) == range_limit, "The number of bars in the histogram does not match the range limit"

    # Check that the plot contains the correct data
    bin_counts, _ = np.histogram(random_numbers, bins=range(1, range_limit + 1))
    for i, bar in enumerate(bars):
        assert bar.get_height() == bin_counts[i], "The height of the bars in the histogram does not match the expected counts"

# Run the tests
if __name__ == "__main__":
    pytest.main()