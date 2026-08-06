import pytest
from src_0614 import task_func

TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
GOALS_RANGE = (-10, 10)

def test_task_func():
    goals = {'Team A': 5, 'Team B': 8, 'Team C': -2, 'Team D': 10, 'Team E': 3}
    penalties = {'Team A': 2, 'Team B': 1, 'Team C': 3, 'Team D': 0, 'Team E': 4}
    expected_scores = {'Team A': 3, 'Team B': 7, 'Team C': -5, 'Team D': 10, 'Team E': -1}

    scores_df = task_func(goals, penalties)

    assert scores_df['Team'].tolist() == TEAMS
    assert scores_df['Score'].tolist() == list(expected_scores.values())

def test_task_func_with_invalid_goals():
    goals = {'Team A': 5, 'Team B': 8, 'Team C': -2, 'Team D': 10, 'Team E': 3}
    penalties = {'Team A': 2, 'Team B': 1, 'Team C': 3, 'Team D': 0, 'Team E': 4}
    invalid_goals = {'Team F': 15, 'Team G': -16}
    goals.update(invalid_goals)

    with pytest.raises(ValueError) as excinfo:
        task_func(goals, penalties)

    assert 'Goals are out of range' in str(excinfo.value)

def test_task_func_with_invalid_penalties():
    goals = {'Team A': 5, 'Team B': 8, 'Team C': -2, 'Team D': 10, 'Team E': 3}
    penalties = {'Team A': 2, 'Team B': 1, 'Team C': 3, 'Team D': 0, 'Team E': 4}
    invalid_penalties = {'Team F': -5, 'Team G': 10}
    penalties.update(invalid_penalties)

    with pytest.raises(ValueError) as excinfo:
        task_func(goals, penalties)

    assert 'Penalties are out of range' in str(excinfo.value)