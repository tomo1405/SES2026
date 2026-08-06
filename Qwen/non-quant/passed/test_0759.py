import pytest
from src_0759 import task_func
import pandas as pd
import numpy as np

def test_task_func_invalid_num_samples():
    with pytest.raises(ValueError):
        task_func('not_an_int')

def test_task_func_default_parameters():
    df = task_func(5)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5
    assert 'Country' in df.columns
    assert 'Age' in df.columns
    assert 'Gender' in df.columns

def test_task_func_custom_parameters():
    df = task_func(10, countries=['France', 'Germany'], ages=np.arange(20, 40), genders=['Other'])
    assert len(df) == 10
    assert df['Country'].isin(['France', 'Germany']).all()
    assert df['Age'].between(20, 39).all()
    assert df['Gender'].unique() == [0]  # Assuming 'Other' is encoded as 0

def test_task_func_random_seed():
    df1 = task_func(5, rng_seed=42)
    df2 = task_func(5, rng_seed=42)
    assert df1.equals(df2)

def test_task_func_gender_encoding():
    df = task_func(5, genders=['Male', 'Female'])
    assert df['Gender'].isin([0, 1]).all()  # Assuming 'Male' is 0 and 'Female' is 1

def test_task_func_empty_countries():
    with pytest.raises(ValueError):
        task_func(5, countries=[])

def test_task_func_empty_ages():
    with pytest.raises(ValueError):
        task_func(5, ages=[])

def test_task_func_empty_genders():
    with pytest.raises(ValueError):
        task_func(5, genders=[])