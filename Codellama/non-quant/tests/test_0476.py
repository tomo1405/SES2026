import matplotlib
import pandas as pd
import pytest
from src_0476 import task_func


def test_task_func_valid_inputs():
    data = pd.DataFrame({'dates': ['2022-01-01', '2022-01-02', '2022-01-03']})
    date_format = '%Y-%m-%d'
    country = 'Russia'
    country_codes = {'Russia': 'ru_RU'}
    ax = task_func(data, date_format, country, country_codes)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_title() == 'Date Distribution'
    assert ax.get_ylabel() == 'Frequency'

def test_task_func_invalid_inputs():
    data = pd.DataFrame({'dates': ['2022-01-01', '2022-01-02', '2022-01-03']})
    date_format = '%Y-%m-%d'
    country = 'Russia'
    country_codes = {'Russia': 'ru_RU'}
    with pytest.raises(ValueError):
        task_func(data, date_format, country, country_codes)

def test_task_func_invalid_date_format():
    data = pd.DataFrame({'dates': ['2022-01-01', '2022-01-02', '2022-01-03']})
    date_format = '%Y-%m-%d'
    country = 'Russia'
    country_codes = {'Russia': 'ru_RU'}
    with pytest.raises(ValueError):
        task_func(data, date_format, country, country_codes)

def test_task_func_invalid_country():
    data = pd.DataFrame({'dates': ['2022-01-01', '2022-01-02', '2022-01-03']})
    date_format = '%Y-%m-%d'
    country = 'Russia'
    country_codes = {'Russia': 'ru_RU'}
    with pytest.raises(ValueError):
        task_func(data, date_format, country, country_codes)