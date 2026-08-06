import pytest
from src_0616 import task_func
import pandas as pd

def test_task_func_default_rng():
    # Test with default random number generator
    df = task_func(5, 3)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5  # There should be one row per team
    assert all(isinstance(row['Team'], str) for row in df.itertuples())
    assert all(isinstance(row['Match Result'], str) for row in df.itertuples())

def test_task_func_with_seed():
    # Test with a specific seed to ensure reproducibility
    seed_value = 42
    df1 = task_func(5, 3, rng_seed=seed_value)
    df2 = task_func(5, 3, rng_seed=seed_value)
    assert df1.equals(df2)

def test_task_func_negative_inputs():
    # Test with negative inputs for goals and penalties
    df = task_func(-10, -5)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5
    assert all(isinstance(row['Team'], str) for row in df.itertuples())
    assert all(isinstance(row['Match Result'], str) for row in df.itertuples())

def test_task_func_zero_inputs():
    # Test with zero inputs for goals and penalties
    df = task_func(0, 0)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5
    assert all(isinstance(row['Team'], str) for row in df.itertuples())
    assert all(isinstance(row['Match Result'], str) for row in df.itertuples())

def test_task_func_large_numbers():
    # Test with large numbers for goals and penalties
    df = task_func(1000, 500)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5
    assert all(isinstance(row['Team'], str) for row in df.itertuples())
    assert all(isinstance(row['Match Result'], str) for row in df.itertuples())