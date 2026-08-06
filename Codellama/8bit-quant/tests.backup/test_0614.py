import pytest
from src_0614 import task_func

def test_task_func():
    goals = {'Team A': 10, 'Team B': 5, 'Team C': 0, 'Team D': -5, 'Team E': -10}
    penalties = {'Team A': 2, 'Team B': 1, 'Team C': 0, 'Team D': 1, 'Team E': 2}
    expected_scores = {'Team A': 8, 'Team B': 4, 'Team C': 0, 'Team D': -6, 'Team E': -12}

    scores_df = task_func(goals, penalties)

    assert scores_df['Score'].equals(expected_scores)