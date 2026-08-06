import pytest
from src_0614 import task_func
import pandas as pd
import matplotlib.pyplot as plt

# Test cases for task_func
def test_task_func():
    # Test data
    goals = {
        'Team A': 5,
        'Team B': 3,
        'Team C': 7,
        'Team D': 2,
        'Team E': 4
    }
    penalties = {
        'Team A': 2,
        'Team B': 1,
        'Team C': 3,
        'Team D': 0,
        'Team E': 2
    }

    # Call the function
    result = task_func(goals=goals, penalties=penalties)

    # Check the result
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert len(result) == len(goals), "The DataFrame should have the same number of rows as teams"
    assert all(result['Score'].between(*GOALS_RANGE)), "Scores should be within the specified range"

    # Check plotting (commented out for testing)
    # plt.show()

# Run the test
if __name__ == "__main__":
    pytest.main()