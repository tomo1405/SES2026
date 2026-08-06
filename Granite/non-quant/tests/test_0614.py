import pandas as pd
from matplotlib import pyplot as plt
from unittest.mock import patch
from src_0614 import task_func

GOALS_RANGE = (-10, 10)
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']

def test_task_func():
    goals = {'Team A': 5, 'Team B': 8, 'Team C': -2, 'Team D': 10, 'Team E': 0}
    penalties = {'Team A': 2, 'Team B': 1, 'Team C': 3, 'Team D': 0, 'Team E': 5}
    expected_scores = {'Team A': 3, 'Team B': 7, 'Team C': -5, 'Team D': 10, 'Team E': -5}

    with patch('matplotlib.pyplot.show') as mock_show:
        scores_df = task_func(goals, penalties)
        mock_show.assert_called_once()

    assert isinstance(scores_df, pd.DataFrame)
    assert list(scores_df['Team']) == TEAMS
    assert list(scores_df['Score']) == list(expected_scores.values())
    assert scores_df['Score'].min() >= GOALS_RANGE[0]
    assert scores_df['Score'].max() <= GOALS_RANGE[1]