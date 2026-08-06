import pytest
from src_0294 import task_func
import itertools
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    elements = [1, 2, 3, 4]
    subset_size = 2
    ax, combinations, sums = task_func(elements, subset_size)
    
    # Check that the number of combinations is correct
    expected_combinations = list(itertools.combinations(elements, subset_size))
    assert len(combinations) == len(expected_combinations)
    
    # Check that the sums are calculated correctly
    expected_sums = [sum(combination) for combination in expected_combinations]
    assert sums == expected_sums
    
    # Check that the histogram is plotted correctly
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == len(np.unique(sums))

# Run the test
if __name__ == "__main__":
    pytest.main()