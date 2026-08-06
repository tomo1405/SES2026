import pytest
from src_0613 import task_func

def test_task_func():
    # Test with valid inputs
    goals = {'Team A': 10, 'Team B': 5, 'Team C': 15, 'Team D': 20, 'Team E': 25}
    penalties = {'Team A': 2, 'Team B': 3, 'Team C': 1, 'Team D': 0, 'Team E': 1}
    report_df = task_func(goals, penalties)
    assert report_df.shape == (5, 5)
    assert report_df['Team'].tolist() == ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    assert report_df['Goals'].tolist() == [10, 5, 15, 20, 25]
    assert report_df['Penalties'].tolist() == [2, 3, 1, 0, 1]
    assert report_df['Penalties Cost'].tolist() == [200, 600, 300, 0, 500]
    assert report_df['Performance Score'].tolist() == [8, 2, 14, 20, 24]

    # Test with invalid inputs
    with pytest.raises(ValueError):
        task_func({}, {})
    with pytest.raises(ValueError):
        task_func({'Team A': 10}, {'Team B': 5})
    with pytest.raises(ValueError):
        task_func({'Team A': 10, 'Team B': 5}, {'Team A': 2, 'Team C': 1})