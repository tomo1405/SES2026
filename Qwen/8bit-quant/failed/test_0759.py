import pytest
from src_0759 import task_func
import pandas as pd
import numpy as np

def test_task_func_invalid_num_samples():
    with pytest.raises(ValueError, match="num_samples should be an integer."):
        task_func('not_an_int')

def test_task_func_default_parameters():
    df = task_func(10)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 10
    assert 'Country' in df.columns
    assert 'Age' in df.columns
    assert 'Gender' in df.columns

def test_task_func_custom_parameters():
    df = task_func(5, countries=['France', 'Germany'], ages=np.arange(20, 30), genders=['Other'])
    assert len(df) == 5
    assert all(df['Country'].isin(['France', 'Germany']))
    assert all(df['Age'] >= 20) and all(df['Age'] < 30)
    assert all(df['Gender'] == 0)  # Assuming 'Other' is encoded as 0

def test_task_func_random_seed():
    df1 = task_func(10, rng_seed=42)
    df2 = task_func(10, rng_seed=42)
    assert df1.equals(df2)

def test_task_func_no_countries():
    with pytest.raises(ValueError, match="num_samples should be an integer."):
        task_func(0, countries=[])

def test_task_func_no_ages():
    with pytest.raises(ValueError, match="num_samples should be an integer."):
        task_func(0, ages=[])

def test_task_func_no_genders():
    with pytest.raises(ValueError, match="num_samples should be an integer."):
        task_func(0, genders=[])

def test_task_func_large_num_samples():
    df = task_func(1000)
    assert len(df) == 1000