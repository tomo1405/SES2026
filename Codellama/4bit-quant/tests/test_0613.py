import pandas as pd
import pytest
from src_0613 import task_func


def test_task_func():
    # Test with valid inputs
    goals = {'Team A': 10, 'Team B': 20, 'Team C': 30, 'Team D': 40, 'Team E': 50}
    penalties = {'Team A': 5, 'Team B': 10, 'Team C': 15, 'Team D': 20, 'Team E': 25}
    report_df = task_func(goals, penalties)
    assert report_df.equals(pd.DataFrame({
        'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
        'Goals': [10, 20, 30, 40, 50],
        'Penalties': [5, 10, 15, 20, 25],
        'Penalties Cost': [500, 1000, 1500, 2000, 2500],
        'Performance Score': [5, 15, 25, 35, 45]
    }))

    # Test with invalid inputs
    with pytest.raises(ValueError):
        task_func({}, {})
    with pytest.raises(ValueError):
        task_func({'Team A': 10}, {'Team B': 20})
    with pytest.raises(ValueError):
        task_func({'Team A': 10, 'Team B': 20}, {'Team C': 30})

if __name__ == '__main__':
    pytest.main()