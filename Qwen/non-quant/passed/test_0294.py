import pytest
from src_0294 import task_func
import itertools
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    elements = [1, 2, 3, 4]
    subset_size = 2
    
    # Calculate expected combinations and their sums
    expected_combinations = list(itertools.combinations(elements, subset_size))
    expected_sums = [sum(combination) for combination in expected_combinations]
    
    # Call the function
    ax, actual_combinations, actual_sums = task_func(elements, subset_size)
    
    # Check if the returned combinations match the expected ones
    assert set(actual_combinations) == set(expected_combinations), "The combinations do not match the expected output."
    
    # Check if the returned sums match the expected ones
    assert actual_sums == expected_sums, "The sums do not match the expected output."
    
    # Check if the histogram plot is created correctly
    assert isinstance(ax, plt.Axes), "The function did not return a matplotlib Axes object."
    assert len(ax.patches) == len(set(expected_sums)), "The number of bins in the histogram does not match the number of unique sums."
    
    # Clear the plot to avoid interference with other tests
    plt.close()

# Run the tests
if __name__ == "__main__":
    pytest.main()