import pytest
from src_1064 import task_func
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_array():
    return np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def test_task_func(sample_array):
    ax = task_func(sample_array)
    
    # Check if the returned object is a matplotlib Axes
    assert isinstance(ax, plt.Axes)
    
    # Check if the plot has the correct title
    assert ax.get_title() == "Explained Variance Ratio of Principal Components"
    
    # Check if the x-ticks and labels are set correctly
    x_ticks = ax.get_xticks()
    x_tick_labels = ax.get_xticklabels()
    assert np.array_equal(x_ticks, [0])
    assert x_tick_labels[0].get_text() == "PC1"
    
    # Check if the bar plot has one bar
    bars = ax.patches
    assert len(bars) == 1
    
    # Check if the bar height is within a reasonable range (since PCA explained variance can vary)
    bar_height = bars[0].get_height()
    assert 0 <= bar_height <= 1

# Run the tests
if __name__ == "__main__":
    pytest.main()