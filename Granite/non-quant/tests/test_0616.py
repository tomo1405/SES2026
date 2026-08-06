import pandas as pd
from src_0616 import task_func


def test_task_func():
    goals = 10
    penalties = 5
    rng_seed = 42
    expected_result = pd.DataFrame([
        ['Team A', '(6 goals, $5000)'],
        ['Team B', '(7 goals, $7000)'],
        ['Team C', '(8 goals, $9000)'],
        ['Team D', '(9 goals, $11000)'],
        ['Team E', '(10 goals, $13000)']
    ], columns=['Team', 'Match Result'])
    actual_result = task_func(goals, penalties, rng_seed)
    assert actual_result.equals(expected_result)

def test_task_func_default_rng_seed():
    goals = 5
    penalties = 3
    expected_result = pd.DataFrame([
        ['Team A', '(3 goals, $3000)'],
        ['Team B', '(4 goals, $5000)'],
        ['Team C', '(4 goals, $5000)'],
        ['Team D', '(4 goals, $5000)'],
        ['Team E', '(5 goals, $7000)']
    ], columns=['Team', 'Match Result'])
    actual_result = task_func(goals, penalties)
    assert actual_result.equals(expected_result)