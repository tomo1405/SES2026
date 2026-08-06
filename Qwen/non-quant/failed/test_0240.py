import pytest
from src_0240 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def test_task_func():
    # Test with a simple list of tuples
    input_data = [(1, 2), (3, 4), (5, 6)]
    arr, computed_stats, ax = task_func(input_data)
    
    # Check if the array is correctly created
    expected_arr = np.array([2, 4, 6])
    assert np.array_equal(arr, expected_arr)
    
    # Check if the computed statistics are correct
    expected_stats = {
        'mean': 4.0,
        'std': np.std(expected_arr),
        'min': 2,
        'max': 6
    }
    assert computed_stats == expected_stats
    
    # Check if the plot is correctly created
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Histogram with PDF'
    assert len(ax.get_lines()) == 2  # One for histogram and one for PDF

    # Check if the plot is closed
    assert plt.fignum_exists(1) == False

# Run the test
if __name__ == "__main__":
    pytest.main()