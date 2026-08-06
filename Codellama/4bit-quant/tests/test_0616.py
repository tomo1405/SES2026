import pytest
from src_0616 import task_func

def test_task_func():
    # Test with valid inputs
    goals = 10
    penalties = 5
    rng_seed = 1234
    expected_results = [
        ['Team A', '(0 goals, $0)'],
        ['Team B', '(0 goals, $0)'],
        ['Team C', '(0 goals, $0)'],
        ['Team D', '(0 goals, $0)'],
        ['Team E', '(0 goals, $0)']
    ]
    results_df = task_func(goals, penalties, rng_seed)
    assert results_df.equals(expected_results)

    # Test with invalid inputs
    with pytest.raises(ValueError):
        task_func(goals, penalties, rng_seed, invalid_arg=True)

    with pytest.raises(ValueError):
        task_func(goals, penalties, rng_seed, invalid_arg=True)

    with pytest.raises(ValueError):
        task_func(goals, penalties, rng_seed, invalid_arg=True)

    with pytest.raises(ValueError):
        task_func(goals, penalties, rng_seed, invalid_arg=True)

    with pytest.raises(ValueError):
        task_func(goals, penalties, rng_seed, invalid_arg=True)