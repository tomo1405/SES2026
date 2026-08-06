import pytest
from src_0617 import task_func

def test_task_func():
    # Test with default parameters
    results_df, ax = task_func(10, 5)
    assert results_df.shape == (5, 3)
    assert ax.get_ylabel() == 'Results'
    assert ax.get_xlabel() == 'Team'
    assert ax.get_ylim() == (0, 10)
    assert ax.get_xlim() == (0, 5)

    # Test with custom parameters
    results_df, ax = task_func(10, 5, teams=['Team A', 'Team B', 'Team C'], penalty_cost=500, rng_seed=123)
    assert results_df.shape == (3, 3)
    assert ax.get_ylabel() == 'Results'
    assert ax.get_xlabel() == 'Team'
    assert ax.get_ylim() == (0, 10)
    assert ax.get_xlim() == (0, 5)

    # Test with negative goals and penalties
    results_df, ax = task_func(-10, -5)
    assert results_df.shape == (5, 3)
    assert ax.get_ylabel() == 'Results'
    assert ax.get_xlabel() == 'Team'
    assert ax.get_ylim() == (0, 10)
    assert ax.get_xlim() == (0, 5)