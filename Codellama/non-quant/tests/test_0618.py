import pytest
from src_0618 import task_func

def test_task_func():
    # Test with default values
    results_df = task_func(goals=10, penalties=5)
    assert results_df.shape == (5, 3)
    assert results_df.columns.tolist() == ['Team', 'Match Result', 'Goals']
    assert results_df['Goals'].dtype == int
    assert results_df['Penalty Cost'].dtype == int

    # Test with custom values
    results_df = task_func(goals=10, penalties=5, rng_seed=42)
    assert results_df.shape == (5, 3)
    assert results_df.columns.tolist() == ['Team', 'Match Result', 'Goals']
    assert results_df['Goals'].dtype == int
    assert results_df['Penalty Cost'].dtype == int

    # Test with custom teams
    results_df = task_func(goals=10, penalties=5, teams=['Team A', 'Team B', 'Team C'])
    assert results_df.shape == (3, 3)
    assert results_df.columns.tolist() == ['Team', 'Match Result', 'Goals']
    assert results_df['Goals'].dtype == int
    assert results_df['Penalty Cost'].dtype == int

    # Test with empty teams
    results_df = task_func(goals=10, penalties=5, teams=[])
    assert results_df.empty