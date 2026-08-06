import pytest
from src_0240 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Test with a simple list of tuples
    input_data = [(1, 2), (2, 3), (3, 4)]
    expected_array = np.array([2, 3, 4])
    expected_stats = {
        'mean': np.mean(expected_array),
        'std': np.std(expected_array),
        'min': np.min(expected_array),
        'max': np.max(expected_array)
    }
    
    result_array, result_stats, result_ax = task_func(input_data)
    
    # Check if the returned array is correct
    assert np.array_equal(result_array, expected_array), "The returned array does not match the expected array."
    
    # Check if the computed statistics are correct
    for key in expected_stats:
        assert np.isclose(result_stats[key], expected_stats[key]), f"The computed {key} does not match the expected value."
    
    # Check if the axis object is a matplotlib AxesSubplot
    assert isinstance(result_ax, plt.Axes), "The returned axis object is not a matplotlib AxesSubplot."

# Run the tests
if __name__ == "__main__":
    pytest.main()