python
import pytest
from src_0616 import task_func

def test_task_func():
    # Test case 1: Normal case
    results_df = task_func(goals=5, penalties=3)
    assert len(results_df) == 5
    assert results_df.shape == (5, 2)
    assert results_df.iloc[0, 1] == '(0 goals, $0)'
    assert results_df.iloc[1, 1] == '(0 goals, $0)'
    assert results_df.iloc[2, 1] == '(0 goals, $0)'
    assert results_df.iloc[3, 1] == '(0 goals, $0)'
    assert results_df.iloc[4, 1] == '(0 goals, $0)'

    # Test case 2: Goals and penalties are negative
    results_df = task_func(goals=-5, penalties=-3)
    assert len(results_df) == 5
    assert results_df.shape == (5, 2)
    assert results_df.iloc[0, 1] == '(0 goals, $0)'
    assert results_df.iloc[1, 1] == '(0 goals, $0)'
    assert results_df.iloc[2, 1] == '(0 goals, $0)'
    assert results_df.iloc[3, 1] == '(0 goals, $0)'
    assert results_df.iloc[4, 1] == '(0 goals, $0)'

    # Test case 3: Goals and penalties are zero
    results_df = task_func(goals=0, penalties=0)
    assert len(results_df) == 5
    assert results_df.shape == (5, 2)
    assert results_df.iloc[0, 1] == '(0 goals, $0)'
    assert results_df.iloc[1, 1] == '(0 goals, $0)'
    assert results_df.iloc[2, 1] == '(0 goals, $0)'
    assert results_df.iloc[3, 1] == '(0 goals, $0)'
    assert results_df.iloc[4, 1] == '(0 goals, $0)'

    # Test case 4: Goals and penalties are positive
    results_df = task_func(goals=5, penalties=3)
    assert len(results_df) == 5
    assert results_df.shape == (5, 2)
    assert results_df.iloc[0, 1] == '(0 goals, $0)'
    assert results_df.iloc[1, 1] == '(0 goals, $0)'
    assert results_df.iloc[2, 1] == '(0 goals, $0)'
    assert results_df.iloc[3, 1] == '(0 goals, $0)'
    assert results_df.iloc[4, 1] == '(0 goals, $0)'

    # Test case 5: Random seed is set
    results_df = task_func(goals=5, penalties=3, rng_seed=42)
    assert len(results_df) == 5
    assert results_df.shape == (5, 2)
    assert results_df.iloc[0, 1] == '(0 goals, $0)'
    assert results_df.iloc[1, 1] == '(0 goals, $0)'
    assert results_df.iloc[2, 1] == '(0 goals, $0)'
    assert results_df.iloc[3, 1] == '(0 goals, $0)'
    assert results_df.iloc[4, 1] == '(0 goals, $0)'