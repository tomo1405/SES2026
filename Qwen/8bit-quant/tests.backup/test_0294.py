import pytest
from src_0294 import task_func
import itertools
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Test with a simple case
    elements = [1, 2, 3]
    subset_size = 2
    ax, combinations, sums = task_func(elements, subset_size)
    
    # Check the combinations
    expected_combinations = list(itertools.combinations(elements, subset_size))
    assert combinations == expected_combinations
    
    # Check the sums
    expected_sums = [sum(combination) for combination in expected_combinations]
    assert sums == expected_sums
    
    # Check the histogram
    # Since we cannot directly check the plot, we can check the data used to create it
    n, bins, patches = ax.get_histgram()
    expected_n, expected_bins = np.histogram(sums, bins=np.arange(min(sums), max(sums) + 2) - 0.5)
    assert np.array_equal(n, expected_n)
    assert np.array_equal(bins, expected_bins)

# Run the tests
if __name__ == "__main__":
    pytest.main()