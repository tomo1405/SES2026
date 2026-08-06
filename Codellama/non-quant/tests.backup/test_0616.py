import pytest
from src_0616 import task_func

def test_task_func():
    # Test with valid inputs
    goals = 10
    penalties = 5
    rng_seed = 1234
    expected_results = [
        ['Team A', '(0 goals, $0)'],
        ['Team B', '(1 goals, $500)'],
        ['Team C', '(2 goals, $1000)'],
        ['Team D', '(3 goals, $1500)'],
        ['Team E', '(4 goals, $2000)']
    ]
    results_df = task_func(goals, penalties, rng_seed)
    assert results_df.equals(expected_results)

    # Test with invalid inputs
    with pytest.raises(ValueError):
        task_func(goals, penalties, rng_seed=None)

    with pytest.raises(ValueError):
        task_func(goals, penalties, rng_seed='abc')

    with pytest.raises(ValueError):
        task_func(goals, penalties, rng_seed=1234.5)