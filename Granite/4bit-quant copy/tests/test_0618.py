import pytest
from src_0618 import task_func

def test_task_func():
    goals = 5
    penalties = 3
    rng_seed = 42
    teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    expected_results = pd.DataFrame([
        ['Team A', '(2 goals, $3000)'],
        ['Team B', '(3 goals, $4000)'],
        ['Team C', '(4 goals, $5000)'],
        ['Team D', '(1 goals, $1000)'],
        ['Team E', '(5 goals, $6000)']
    ], columns=['Team', 'Match Result'])
    pd.testing.assert_frame_equal(task_func(goals, penalties, rng_seed, teams), expected_results)

def test_task_func_empty_df():
    goals = 1
    penalties = 1
    rng_seed = 42
    teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    expected_results = pd.DataFrame(columns=['Team', 'Match Result'])
    pd.testing.assert_frame_equal(task_func(goals, penalties, rng_seed, teams), expected_results)

def test_task_func_invalid_goals():
    with pytest.raises(ValueError):
        task_func(-1, 3)

def test_task_func_invalid_penalties():
    with pytest.raises(ValueError):
        task_func(5, -1)