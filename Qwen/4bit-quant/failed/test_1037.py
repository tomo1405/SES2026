import pytest
from src_1037 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    # Create sample series
    s1 = pd.Series(np.random.randn(10), name='Series1')
    s2 = pd.Series(np.random.randn(10), name='Series2')

    # Ensure there is at least one intersection point
    s1.iloc[0] = s2.iloc[0]

    # Call the function
    ax, intersection_count = task_func(s1, s2)

    # Check if the intersection count is correct
    expected_intersection_count = len(set(s1).intersection(set(s2)))
    assert intersection_count == expected_intersection_count, f"Expected {expected_intersection_count}, got {intersection_count}"

    # Check if the plot is created correctly (basic check)
    assert ax is not None, "Plot axis is None"
    assert isinstance(ax, plt.Axes), "ax is not an instance of plt.Axes"

    # Additional checks can be added here if necessary

# Run the tests
if __name__ == "__main__":
    pytest.main()