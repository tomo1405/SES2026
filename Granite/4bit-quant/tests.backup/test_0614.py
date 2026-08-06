import pandas as pd
from matplotlib import pyplot as plt
from src_0614 import task_func

TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
GOALS_RANGE = (-10, 10)

def test_task_func():
    goals = {'Team A': 5, 'Team B': 8, 'Team C': -3, 'Team D': 10, 'Team E': 0}
    penalties = {'Team A': 2, 'Team B': 1, 'Team C': 5, 'Team D': 0, 'Team E': 3}
    expected_scores = {'Team A': 3, 'Team B': 7, 'Team C': -8, 'Team D': 10, 'Team E': -3}

    scores_df = task_func(goals, penalties)

    assert scores_df['Team'].tolist() == TEAMS
    assert scores_df['Score'].tolist() == list(expected_scores.values())
    assert scores_df['Score'].min() >= GOALS_RANGE[0]
    assert scores_df['Score'].max() <= GOALS_RANGE[1]

def test_task_func_with_invalid_inputs():
    goals = {'Team A': 5, 'Team B': 8, 'Team C': -3, 'Team D': 10, 'Team E': 0}
    penalties = {'Team A': 2, 'Team B': 1, 'Team C': 5, 'Team D': 0, 'Team E': 3}
    invalid_goals = {'Team F': 15, 'Team G': -15}
    invalid_penalties = {'Team F': 2, 'Team G': 1}

    with pytest.raises(ValueError):
        task_func(invalid_goals, penalties)

    with pytest.raises(ValueError):
        task_func(goals, invalid_penalties)

    with pytest.raises(ValueError):
        task_func(invalid_goals, invalid_penalties)