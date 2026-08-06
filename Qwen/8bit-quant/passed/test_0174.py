import pytest
from src_0174 import task_func
import numpy as np
import pandas as pd

def test_task_func():
    # Test with all countries in the list
    country_dict = {'country1': 'USA', 'country2': 'UK'}
    result = task_func(country_dict)
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 2
    assert 'GDP' in result.columns
    assert result.index.tolist() == ['USA', 'UK']
    assert result['GDP'].dtype == np.int64

    # Test with no countries in the list
    country_dict = {'country1': 'Canada', 'country2': 'Germany'}
    result = task_func(country_dict)
    assert isinstance(result, pd.DataFrame)
    assert result.empty

    # Test with some countries in the list
    country_dict = {'country1': 'USA', 'country2': 'Germany', 'country3': 'China'}
    result = task_func(country_dict)
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 2
    assert 'GDP' in result.columns
    assert result.index.tolist() == ['USA', 'China']
    assert result['GDP'].dtype == np.int64

    # Test with duplicate countries in the list
    country_dict = {'country1': 'USA', 'country2': 'USA', 'country3': 'China'}
    result = task_func(country_dict)
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 2
    assert 'GDP' in result.columns
    assert result.index.tolist() == ['USA', 'China']
    assert result['GDP'].dtype == np.int64