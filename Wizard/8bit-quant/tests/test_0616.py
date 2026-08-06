python
import pytest
from src_0616 import task_func

def test_task_func():
    # Test case 1: Normal case
    results_df = task_func(goals=5, penalties=2)
    assert isinstance(results_df, pd.DataFrame)
    assert len(results_df) == 5
    assert results_df.shape[1] == 2
    assert results_df.iloc[0, 0] == 'Team A'
    assert results_df.iloc[0, 1] == '(3 goals, $3000)'
    assert results_df.iloc[1, 0] == 'Team B'
    assert results_df.iloc[1, 1] == '(1 goals, $1000)'
    assert results_df.iloc[2, 0] == 'Team C'
    assert results_df.iloc[2, 1] == '(1 goals, $1000)'
    assert results_df.iloc[3, 0] == 'Team D'
    assert results_df.iloc[3, 1] == '(0 goals, $0)'
    assert results_df.iloc[4, 0] == 'Team E'
    assert results_df.iloc[4, 1] == '(0 goals, $0)'

    # Test case 2: No goals scored
    results_df = task_func(goals=0, penalties=2)
    assert isinstance(results_df, pd.DataFrame)
    assert len(results_df) == 5
    assert results_df.shape[1] == 2
    assert results_df.iloc[0, 0] == 'Team A'
    assert results_df.iloc[0, 1] == '(0 goals, $2000)'
    assert results_df.iloc[1, 0] == 'Team B'
    assert results_df.iloc[1, 1] == '(0 goals, $1000)'
    assert results_df.iloc[2, 0] == 'Team C'
    assert results_df.iloc[2, 1] == '(0 goals, $1000)'
    assert results_df.iloc[3, 0] == 'Team D'
    assert results_df.iloc[3, 1] == '(0 goals, $0)'
    assert results_df.iloc[4, 0] == 'Team E'
    assert results_df.iloc[4, 1] == '(0 goals, $0)'

    # Test case 3: No penalties
    results_df = task_func(goals=5, penalties=0)
    assert isinstance(results_df, pd.DataFrame)
    assert len(results_df) == 5
    assert results_df.shape[1] == 2
    assert results_df.iloc[0, 0] == 'Team A'
    assert results_df.iloc[0, 1] == '(5 goals, $0)'
    assert results_df.iloc[1, 0] == 'Team B'
    assert results_df.iloc[1, 1] == '(0 goals, $0)'
    assert results_df.iloc[2, 0] == 'Team C'
    assert results_df.iloc[2, 1] == '(0 goals, $0)'
    assert results_df.iloc[3, 0] == 'Team D'
    assert results_df.iloc[3, 1] == '(0 goals, $0)'
    assert results_df.iloc[4, 0] == 'Team E'
    assert results_df.iloc[4, 1] == '(0 goals, $0)'

    # Test case 4: No goals or penalties scored
    results_df = task_func(goals=0, penalties=0)
    assert isinstance(results_df, pd.DataFrame)
    assert len(results_df) == 5
    assert results_df.shape[1] == 2
    assert results_df.iloc[0, 0] == 'Team A'
    assert results_df.iloc[0, 1] == '(0 goals, $0)'
    assert results_df.iloc[1, 0] == 'Team B'
    assert results_df.iloc[1, 1] == '(0 goals, $0)'
    assert results_df.iloc[2, 0] == 'Team C'
    assert results_df.iloc[2, 1] == '(0 goals, $0)'
    assert results_df.iloc[3, 0] == 'Team D'
    assert results_df.iloc[3, 1] == '(0 goals, $0)'
    assert results_df.iloc[4, 0] == 'Team E'
    assert results_df.iloc[4, 1] == '(0 goals, $0)'

    # Test case 5: Random seed
    results_df = task_func(goals=5, penalties=2, rng_seed=42)
    assert isinstance(results_df, pd.DataFrame)
    assert len(results_df) == 5
    assert results_df.shape[1] == 2
    assert results_df.iloc[0, 0] == 'Team A'
    assert results_df.iloc[0, 1] == '(3 goals, $3000)'
    assert results_df.iloc[1, 0] == 'Team B'
    assert results_df.iloc[1, 1] == '(1 goals, $1000)'
    assert results_df.iloc[2, 0] == 'Team C'
    assert results_df.iloc[2, 1] == '(1 goals, $1000)'
    assert results_df.iloc[3, 0] == 'Team D'
    assert results_df.iloc[3, 1] == '(0 goals, $0)'
    assert results_df.iloc[4, 0] == 'Team E'
    assert results_df.iloc[4, 1] == '(0 goals, $0)'