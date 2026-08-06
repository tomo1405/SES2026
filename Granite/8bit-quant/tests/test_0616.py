import pandas as pd
from src_0616 import task_func


def test_task_func():
    goals = 10
    penalties = 5
    rng_seed = 42
    expected_result = pd.DataFrame([
        ['Team A', '(10 goals, $5000)'],
        ['Team B', '(8 goals, $4000)'],
        ['Team C', '(6 goals, $3000)'],
        ['Team D', '(4 goals, $2000)'],
        ['Team E', '(2 goals, $1000)']
    ], columns=['Team', 'Match Result'])
    actual_result = task_func(goals, penalties, rng_seed)
    assert actual_result.equals(expected_result)

def test_task_func_default_rng_seed():
    goals = 5
    penalties = 3
    expected_result = pd.DataFrame([
        ['Team A', '(5 goals, $3000)'],
        ['Team B', '(4 goals, $2000)'],
        ['Team C', '(3 goals, $1000)'],
        ['Team D', '(2 goals, $0)'],
        ['Team E', '(1 goal, $0)']
    ], columns=['Team', 'Match Result'])
    actual_result = task_func(goals, penalties)
    assert actual_result.equals(expected_result)