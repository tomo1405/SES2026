python
import pytest
from src_0613 import task_func

def test_task_func():
    goals = {'Team A': 5, 'Team B': 3, 'Team C': 2, 'Team D': 0, 'Team E': 1}
    penalties = {'Team A': 1, 'Team B': 2, 'Team C': 0, 'Team D': 1, 'Team E': 0}
    report_df = task_func(goals, penalties)
    assert report_df.shape == (5, 5)
    assert report_df['Team'].tolist() == ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    assert report_df['Goals'].tolist() == [5, 3, 2, 0, 1]
    assert report_df['Penalties'].tolist() == [1, 2, 0, 1, 0]
    assert report_df['Penalties Cost'].tolist() == [100, 400, 0, 200, 0]
    assert report_df['Performance Score'].tolist() == [4, 1, 2, 0, 1]