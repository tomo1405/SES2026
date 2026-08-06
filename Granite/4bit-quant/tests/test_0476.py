import pandas as pd
import pytest
from src_0476 import task_func


def test_task_func_valid_input():
    data = pd.DataFrame({'dates': ['2022-01-01', '2022-01-02', '2022-01-03']})
    date_format = '%Y-%m-%d'
    country = 'Russia'
    country_codes = {'Russia': 'ru_RU'}
    ax = task_func(data, date_format, country, country_codes)
    assert ax is not None

def test_task_func_invalid_input_types():
    data = 'not a DataFrame'
    date_format = 123
    country = 'Russia'
    country_codes = {'Russia': 'ru_RU'}
    with pytest.raises(ValueError, match="Invalid input types."):
        task_func(data, date_format, country, country_codes)

def test_task_func_invalid_country_code():
    data = pd.DataFrame({'dates': ['2022-01-01', '2022-01-02', '2022-01-03']})
    date_format = '%Y-%m-%d'
    country = 'USA'
    country_codes = {'Russia': 'ru_RU'}
    with pytest.raises(ValueError, match=r"Country 'USA' not found in country codes."):
        task_func(data, date_format, country, country_codes)

def test_task_func_invalid_date_format():
    data = pd.DataFrame({'dates': ['2022-01-01', '2022-01-02', '2022-01-03']})
    date_format = '%Y-%m'
    country = 'Russia'
    country_codes = {'Russia': 'ru_RU'}
    with pytest.raises(ValueError, match="Date format mismatch."):
        task_func(data, date_format, country, country_codes)