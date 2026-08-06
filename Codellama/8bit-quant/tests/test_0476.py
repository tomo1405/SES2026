import matplotlib
import pandas as pd
import pytest
from src_0476 import task_func


def test_task_func_valid_input():
    data = pd.DataFrame({'dates': ['2022-01-01', '2022-01-02', '2022-01-03']})
    date_format = '%Y-%m-%d'
    country = 'Russia'
    country_codes = {'Russia': 'ru_RU'}
    ax = task_func(data, date_format, country, country_codes)
    assert isinstance(ax, matplotlib.axes.Axes)

def test_task_func_invalid_input_data():
    data = 'invalid_data'
    date_format = '%Y-%m-%d'
    country = 'Russia'
    country_codes = {'Russia': 'ru_RU'}
    with pytest.raises(ValueError):
        task_func(data, date_format, country, country_codes)

def test_task_func_invalid_input_date_format():
    data = pd.DataFrame({'dates': ['2022-01-01', '2022-01-02', '2022-01-03']})
    date_format = 'invalid_date_format'
    country = 'Russia'
    country_codes = {'Russia': 'ru_RU'}
    with pytest.raises(ValueError):
        task_func(data, date_format, country, country_codes)

def test_task_func_invalid_input_country():
    data = pd.DataFrame({'dates': ['2022-01-01', '2022-01-02', '2022-01-03']})
    date_format = '%Y-%m-%d'
    country = 'Invalid_Country'
    country_codes = {'Russia': 'ru_RU'}
    with pytest.raises(ValueError):
        task_func(data, date_format, country, country_codes)

def test_task_func_invalid_input_country_codes():
    data = pd.DataFrame({'dates': ['2022-01-01', '2022-01-02', '2022-01-03']})
    date_format = '%Y-%m-%d'
    country = 'Russia'
    country_codes = 'invalid_country_codes'
    with pytest.raises(ValueError):
        task_func(data, date_format, country, country_codes)