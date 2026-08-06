import pytest
from src_0617 import task_func

def test_task_func():
    goals = 10
    penalties = 5
    rng_seed = 42
    teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    penalty_cost = 1000
    expected_results = [
        ['Team A', 5, 2000],
        ['Team B', 7, 1400],
        ['Team C', 3, 300],
        ['Team D', 8, 1600],
        ['Team E', 2, 200]
    ]
    expected_df = pd.DataFrame(expected_results, columns=['Team', 'Goals', 'Penalty Cost'])

    results_df, ax = task_func(goals, penalties, teams, penalty_cost, rng_seed)

    assert results_df.equals(expected_df)
    assert ax is not None

def test_task_func_default_args():
    goals = 10
    penalties = 5
    expected_results = [
        ['Team A', 5, 5000],
        ['Team B', 7, 3500],
        ['Team C', 3, 300],
        ['Team D', 8, 4000],
        ['Team E', 2, 200]
    ]
    expected_df = pd.DataFrame(expected_results, columns=['Team', 'Goals', 'Penalty Cost'])

    results_df, ax = task_func(goals, penalties)

    assert results_df.equals(expected_df)
    assert ax is not None

def test_task_func_invalid_args():
    with pytest.raises(ValueError):
        task_func(-10, 5)

    with pytest.raises(ValueError):
        task_func(10, -5)

    with pytest.raises(ValueError):
        task_func(10, 5, teams=['Team A'])