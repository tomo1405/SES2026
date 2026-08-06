import pandas as pd
from src_0618 import task_func


def test_task_func_returns_dataframe():
    results_df = task_func(goals=10, penalties=5, rng_seed=123)
    assert isinstance(results_df, pd.DataFrame)

def test_task_func_returns_correct_number_of_rows():
    results_df = task_func(goals=10, penalties=5, rng_seed=123)
    assert len(results_df) == 5

def test_task_func_returns_correct_number_of_columns():
    results_df = task_func(goals=10, penalties=5, rng_seed=123)
    assert len(results_df.columns) == 3

def test_task_func_returns_correct_data():
    results_df = task_func(goals=10, penalties=5, rng_seed=123)
    expected_results = [
        ['Team A', '(3 goals, $500)'],
        ['Team B', '(4 goals, $500)'],
        ['Team C', '(5 goals, $500)'],
        ['Team D', '(6 goals, $500)'],
        ['Team E', '(7 goals, $500)']
    ]
    assert results_df.values.tolist() == expected_results

def test_task_func_returns_correct_data_with_different_seed():
    results_df = task_func(goals=10, penalties=5, rng_seed=456)
    expected_results = [
        ['Team A', '(3 goals, $500)'],
        ['Team B', '(4 goals, $500)'],
        ['Team C', '(5 goals, $500)'],
        ['Team D', '(6 goals, $500)'],
        ['Team E', '(7 goals, $500)']
    ]
    assert results_df.values.tolist() == expected_results

def test_task_func_returns_correct_data_with_different_teams():
    results_df = task_func(goals=10, penalties=5, rng_seed=123, teams=['Team A', 'Team B', 'Team C'])
    expected_results = [
        ['Team A', '(3 goals, $500)'],
        ['Team B', '(4 goals, $500)'],
        ['Team C', '(5 goals, $500)']
    ]
    assert results_df.values.tolist() == expected_results

def test_task_func_returns_correct_data_with_different_goals():
    results_df = task_func(goals=15, penalties=5, rng_seed=123)
    expected_results = [
        ['Team A', '(3 goals, $500)'],
        ['Team B', '(4 goals, $500)'],
        ['Team C', '(5 goals, $500)'],
        ['Team D', '(6 goals, $500)'],
        ['Team E', '(7 goals, $500)']
    ]
    assert results_df.values.tolist() == expected_results

def test_task_func_returns_correct_data_with_different_penalties():
    results_df = task_func(goals=10, penalties=10, rng_seed=123)
    expected_results = [
        ['Team A', '(3 goals, $500)'],
        ['Team B', '(4 goals, $500)'],
        ['Team C', '(5 goals, $500)'],
        ['Team D', '(6 goals, $500)'],
        ['Team E', '(7 goals, $500)']
    ]
    assert results_df.values.tolist() == expected_results