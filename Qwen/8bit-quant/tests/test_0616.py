import pandas as pd
from src_0616 import task_func


def test_task_func_default_behavior():
    # Test with default parameters
    df = task_func(5, 3)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5
    assert 'Team' in df.columns
    assert 'Match Result' in df.columns

def test_task_func_with_seed():
    # Test with a specific seed for reproducibility
    df1 = task_func(5, 3, rng_seed=42)
    df2 = task_func(5, 3, rng_seed=42)
    assert df1.equals(df2)

def test_task_func_negative_goals():
    # Test with negative goals
    df = task_func(-5, 3)
    assert all(df['Match Result'].str.contains(r'\d+ goals'))

def test_task_func_negative_penalties():
    # Test with negative penalties
    df = task_func(5, -3)
    assert all(df['Match Result'].str.contains(r'\$\d+'))

def test_task_func_zero_goals_and_penalties():
    # Test with zero goals and penalties
    df = task_func(0, 0)
    assert all(df['Match Result'] == '(0 goals, $0)')

def test_task_func_no_penalties():
    # Test with no penalties
    df = task_func(5, 0)
    assert all(df['Match Result'].str.endswith('$(0)'))

def test_task_func_no_goals():
    # Test with no goals
    df = task_func(0, 3)
    assert all(df['Match Result'].str.startswith('(0 goals'))