python
import pandas as pd
import pytest
from src_0614 import task_func

# Constants
GOALS = {'Team A': 5, 'Team B': 3, 'Team C': 0, 'Team D': -2, 'Team E': 1}
PENALTIES = {'Team A': 0, 'Team B': 1, 'Team C': 0, 'Team D': 0, 'Team E': 0}

# Test case 1
def test_task_func_valid_input():
    expected_output = pd.DataFrame([['Team A', 5], ['Team B', 2], ['Team C', 0], ['Team D', -2], ['Team E', 1]], columns=['Team', 'Score'])
    assert task_func(GOALS, PENALTIES).equals(expected_output)

# Test case 2
def test_task_func_invalid_input():
    with pytest.raises(TypeError):
        task_func('invalid_input', PENALTIES)

# Test case 3
def test_task_func_empty_input():
    with pytest.raises(ValueError):
        task_func({}, {})

# Test case 4
def test_task_func_no_goal_input():
    with pytest.raises(ValueError):
        task_func({'Team A': 0, 'Team B': 0, 'Team C': 0, 'Team D': 0, 'Team E': 0}, PENALTIES)

# Test case 5
def test_task_func_no_penalty_input():
    with pytest.raises(ValueError):
        task_func(GOALS, {'Team A': 0, 'Team B': 0, 'Team C': 0, 'Team D': 0, 'Team E': 0})

# Test case 6
def test_task_func_no_score_input():
    with pytest.raises(ValueError):
        task_func({'Team A': 0, 'Team B': 0, 'Team C': 0, 'Team D': 0, 'Team E': 0}, {'Team A': 0, 'Team B': 0, 'Team C': 0, 'Team D': 0, 'Team E': 0})

# Test case 7
def test_task_func_no_team_input():
    with pytest.raises(ValueError):
        task_func({'Team A': 0, 'Team B': 0, 'Team C': 0, 'Team D': 0, 'Team E': 0}, {'Team A': 0, 'Team B': 0, 'Team C': 0, 'Team D': 0})

# Test case 8
def test_task_func_no_goal_or_penalty_input():
    with pytest.raises(ValueError):
        task_func({'Team A': 0, 'Team B': 0, 'Team C': 0, 'Team D': 0, 'Team E': 0}, {})

# Test case 9
def test_task_func_no_goal_or_score_input():
    with pytest.raises(ValueError):
        task_func({'Team A': 0, 'Team B': 0, 'Team C': 0, 'Team D': 0, 'Team E': 0}, {'Team A': 0, 'Team B': 0, 'Team C': 0, 'Team D': 0, 'Team E': 0, 'Team F': 0})

# Test case 10
def test_task_func_no_penalty_or_score_input():
    with pytest.raises(ValueError):
        task_func({'Team A': 0, 'Team B': 0, 'Team C': 0, 'Team D': 0, 'Team E': 0}, {'Team A': 0, 'Team B': 0, 'Team C': 0, 'Team D': 0})

# Test case 11
def test_task_func_no_team_or_score_input():
    with pytest.raises(ValueError):
        task_func({'Team A': 0, 'Team B': 0, 'Team C': 0, 'Team D': 0, 'Team E': 0}, {'Team A': 0, 'Team B': 0, 'Team C': 0, 'Team D': 0, 'Team E': 0, 'Team F': 0})

# Test case 12
def test_task_func_no_goal_or_penalty_or_score_input():
    with pytest.raises(ValueError):
        task_func({'Team A': 0, 'Team B': 0, 'Team C': 0, 'Team D': 0, 'Team E': 0}, {})

# Test case 13
def test_task_func_no_goal_or_penalty_or_team_input():
    with pytest.raises(ValueError):
        task_func({'Team A': 0, 'Team B': 0, 'Team C': 0, 'Team D': 0, 'Team E': 0}, {})

# Test case 14
def test_task_func_no_goal_or_score_or_team_input():
    with pytest.raises(ValueError):
        task_func({'Team A': 0, 'Team B': 0, 'Team C': 0, 'Team D': 0, 'Team E': 0}, {'Team A': 0, 'Team B': 0, 'Team C': 0, 'Team D': 0, 'Team E': 0, 'Team F': 0})

# Test case 15
def test_task_func_no_penalty_or_score_or_team_input():
    with pytest.raises(ValueError):
        task_func({'Team A': 0, 'Team B': 0, 'Team C': 0, 'Team D': 0, 'Team E': 0}, {'Team A': 0, 'Team B': 0, 'Team C': 0, 'Team D': 0})

# Test case 16
def test_task_func_no_goal_or_penalty_or_score_or_team_input():
    with pytest.raises(ValueError):
        task_func({'Team A': 0, 'Team B': 0, 'Team C': 0, 'Team D': 0, 'Team E': 0}, {})