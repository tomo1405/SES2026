import pytest
from src_0759 import task_func
import pandas as pd
import numpy as np

def test_task_func_output_type():
    result = task_func(5)
    assert isinstance(result, pd.DataFrame), "The output should be a pandas DataFrame."

def test_task_func_columns():
    result = task_func(5)
    expected_columns = ['Country', 'Age', 'Gender']
    assert list(result.columns) == expected_columns, "DataFrame columns do not match expected columns."

def test_task_func_num_samples():
    num_samples = 10
    result = task_func(num_samples)
    assert len(result) == num_samples, "Number of samples in the DataFrame does not match the input."

def test_task_func_countries():
    num_samples = 5
    countries = ['Russia', 'China', 'USA', 'India', 'Brazil']
    result = task_func(num_samples)
    assert all(country in countries for country in result['Country']), "Countries in the DataFrame are not within the specified list."

def test_task_func_ages():
    num_samples = 5
    ages = np.arange(18, 60)
    result = task_func(num_samples)
    assert all(age in ages for age in result['Age']), "Ages in the DataFrame are not within the specified range."

def test_task_func_genders_encoded():
    num_samples = 5
    result = task_func(num_samples)
    assert all(isinstance(gender, int) for gender in result['Gender']), "Genders should be encoded as integers."

def test_task_func_invalid_num_samples():
    with pytest.raises(ValueError):
        task_func('not_an_int')

def test_task_func_with_seed():
    num_samples = 5
    seed = 42
    result1 = task_func(num_samples, rng_seed=seed)
    result2 = task_func(num_samples, rng_seed=seed)
    assert result1.equals(result2), "DataFrames generated with the same seed should be identical."