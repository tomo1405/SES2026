import pytest
from src_0613 import task_func

def test_task_func():
    goals = {'Team A': 10, 'Team B': 5, 'Team C': 15}
    penalties = {'Team A': 2, 'Team B': 3, 'Team C': 1}
    report_df = task_func(goals, penalties)
    assert report_df.shape == (3, 5)
    assert report_df['Team'].tolist() == ['Team A', 'Team B', 'Team C']
    assert report_df['Goals'].tolist() == [10, 5, 15]
    assert report_df['Penalties'].tolist() == [2, 3, 1]
    assert report_df['Penalties Cost'].tolist() == [200, 600, 100]
    assert report_df['Performance Score'].tolist() == [8, 2, 14]