python
import pytest
from src_0616 import task_func

def test_task_func():
    # Test case 1: Normal case
    results_df = task_func(goals=5, penalties=2)
    assert len(results_df) == 5
    assert results_df.shape[1] == 2
    assert results_df['Team'].tolist() == ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    assert results_df['Match Result'].tolist() == ['(3 goals, $3000)', '(2 goals, $2000)', '(1 goals, $1000)', '(0 goals, $0)', '(0 goals, $0)']

    # Test case 2: No goals scored
    results_df = task_func(goals=0, penalties=2)
    assert len(results_df) == 5
    assert results_df.shape[1] == 2
    assert results_df['Team'].tolist() == ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    assert results_df['Match Result'].tolist() == ['(0 goals, $2000)', '(0 goals, $2000)', '(0 goals, $1000)', '(0 goals, $0)', '(0 goals, $0)']

    # Test case 3: No penalties
    results_df = task_func(goals=5, penalties=0)
    assert len(results_df) == 5
    assert results_df.shape[1] == 2
    assert results_df['Team'].tolist() == ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    assert results_df['Match Result'].tolist() == ['(5 goals, $0)', '(5 goals, $0)', '(5 goals, $0)', '(5 goals, $0)', '(5 goals, $0)']

    # Test case 4: No goals or penalties scored
    results_df = task_func(goals=0, penalties=0)
    assert len(results_df) == 5
    assert results_df.shape[1] == 2
    assert results_df['Team'].tolist() == ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    assert results_df['Match Result'].tolist() == ['(0 goals, $0)', '(0 goals, $0)', '(0 goals, $0)', '(0 goals, $0)', '(0 goals, $0)']

    # Test case 5: Random seed
    results_df = task_func(goals=5, penalties=2, rng_seed=42)
    assert len(results_df) == 5
    assert results_df.shape[1] == 2
    assert results_df['Team'].tolist() == ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    assert results_df['Match Result'].tolist() == ['(3 goals, $3000)', '(2 goals, $2000)', '(1 goals, $1000)', '(0 goals, $0)', '(0 goals, $0)']