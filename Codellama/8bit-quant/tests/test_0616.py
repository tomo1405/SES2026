import pytest
from src_0616 import task_func

def test_task_func():
    # Test with valid inputs
    goals = 10
    penalties = 5
    rng_seed = 1234
    results_df = task_func(goals, penalties, rng_seed)
    assert results_df.shape == (5, 2)
    assert results_df.columns.tolist() == ['Team', 'Match Result']
    assert results_df['Team'].tolist() == ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    assert results_df['Match Result'].tolist() == ['(10 goals, $5000)', '(10 goals, $5000)', '(10 goals, $5000)', '(10 goals, $5000)', '(10 goals, $5000)']

    # Test with invalid inputs
    with pytest.raises(ValueError):
        task_func(goals, penalties, rng_seed=None)

    with pytest.raises(ValueError):
        task_func(goals, penalties, rng_seed='abc')

    with pytest.raises(ValueError):
        task_func(goals, penalties, rng_seed=1234.56)