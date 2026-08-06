import pandas as pd
from random import randint, seed
from src_0616 import task_func

def test_task_func():
    goals = 10
    penalties = 5
    rng_seed = 42
    seed(rng_seed)  # Set seed for reproducibility
    results_df = task_func(goals, penalties, rng_seed)
    assert isinstance(results_df, pd.DataFrame)
    assert results_df.shape == (5, 2)
    assert results_df.columns.tolist() == ['Team', 'Match Result']
    expected_results = [
        ('Team A', '(6 goals, $500)'),
        ('Team B', '(7 goals, $700)'),
        ('Team C', '(10 goals, $1000)'),
        ('Team D', '(3 goals, $300)'),
        ('Team E', '(8 goals, $800)')
    ]
    for team, result in expected_results:
        assert (results_df['Team'] == team).any()
        assert (results_df['Match Result'] == result).any()

def test_task_func_default_rng():
    goals = 5
    penalties = 3
    results_df = task_func(goals, penalties)
    assert isinstance(results_df, pd.DataFrame)
    assert results_df.shape == (5, 2)
    assert results_df.columns.tolist() == ['Team', 'Match Result']