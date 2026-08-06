import pytest
from src_0614 import task_func

def test_task_func():
    goals = {'Team A': 5, 'Team B': -3, 'Team C': 7, 'Team D': 2, 'Team E': -8}
    penalties = {'Team A': 2, 'Team B': 1, 'Team C': 3, 'Team D': 5, 'Team E': 4}

    expected_output = pd.DataFrame({
        'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
        'Score': [3, -4, 4, -3, -12]
    })

    result = task_func(goals, penalties)

    # Check if the DataFrame has the correct structure
    assert result.equals(expected_output)

    # Check if the 'Score' column is clipped within the GOALS_RANGE
    assert result['Score'].min() >= -10 and result['Score'].max() <= 10

def test_task_func_missing_teams():
    goals = {'Team A': 5, 'Team C': 7, 'Team E': -8}
    penalties = {'Team A': 2, 'Team B': 1, 'Team D': 5, 'Team E': 4}

    expected_output = pd.DataFrame({
        'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
        'Score': [3, -1, 4, -5, -12]
    })

    result = task_func(goals, penalties)

    assert result.equals(expected_output)

def test_task_func_no_teams():
    goals = {}
    penalties = {}

    expected_output = pd.DataFrame({
        'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
        'Score': [0, 0, 0, 0, 0]
    })

    result = task_func(goals, penalties)

    assert result.equals(expected_output)

def test_task_func_all_teams_with_zero_scores():
    goals = {team: 0 for team in TEAMS}
    penalties = {team: 0 for team in TEAMS}

    expected_output = pd.DataFrame({
        'Team': TEAMS,
        'Score': [0] * len(TEAMS)
    })

    result = task_func(goals, penalties)

    assert result.equals(expected_output)