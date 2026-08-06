import pytest
from src_0174 import task_func
import numpy as np
import pandas as pd

def test_task_func():
    # Test with all countries present
    country_dict = {'country1': 'USA', 'country2': 'UK', 'country3': 'China', 'country4': 'Japan', 'country5': 'Australia'}
    df = task_func(country_dict)
    assert isinstance(df, pd.DataFrame)
    assert list(df.index) == ['USA', 'UK', 'China', 'Japan', 'Australia']
    assert df.shape[1] == 1
    assert all(isinstance(gdp, np.int64) for gdp in df['GDP'])

    # Test with some countries missing
    country_dict = {'country1': 'USA', 'country2': 'France', 'country3': 'China'}
    df = task_func(country_dict)
    assert isinstance(df, pd.DataFrame)
    assert list(df.index) == ['USA', 'China']
    assert df.shape[1] == 1
    assert all(isinstance(gdp, np.int64) for gdp in df['GDP'])

    # Test with no countries present
    country_dict = {'country1': 'Germany', 'country2': 'Russia'}
    df = task_func(country_dict)
    assert isinstance(df, pd.DataFrame)
    assert df.empty
    assert df.shape[1] == 1

    # Test with empty dictionary
    country_dict = {}
    df = task_func(country_dict)
    assert isinstance(df, pd.DataFrame)
    assert df.empty
    assert df.shape[1] == 1