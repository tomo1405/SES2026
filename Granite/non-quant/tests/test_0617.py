import pytest
from src_0617 import task_func

def test_task_func():
    goals = 10
    penalties = 5
    rng_seed = 42
    teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    penalty_cost = 1000
    expected_results_df = ...  # Replace with the expected DataFrame
    expected_ax = ...  # Replace with the expected Axes object

    results_df, ax = task_func(goals, penalties, teams, penalty_cost, rng_seed)

    assert results_df.equals(expected_results_df)
    assert ax == expected_ax