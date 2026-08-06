import pytest
from src_0476 import task_func
import pandas as pd
from datetime import datetime

def test_task_func_valid_data():
    data = pd.DataFrame({'dates': ['2023-01-01', '2023-02-01', '2023-03-01']})
    date_format = '%Y-%m-%d'
    country = 'Russia'
    ax = task_func(data, date_format, country)
    assert isinstance(ax, pd.plotting._matplotlib.hist.Plot)
    assert 'Date Distribution' in ax.get_title()
    assert 'Frequency' in ax.get_ylabel()

def test_task_func_invalid_date_format():
    data = pd.DataFrame({'dates': ['2023-01-01', '2023-02-01', '2023-03-01']})
    date_format = '%Y/%m/%d'
    country = 'Russia'
    with pytest.raises(ValueError, match="Date format mismatch."):
        task_func(data, date_format, country)

def test_task_func_invalid_country():
    data = pd.DataFrame({'dates': ['2023-01-01', '2023-02-01', '2023-03-01']})
    date_format = '%Y-%m-%d'
    country = 'Unknown'
    with pytest.raises(ValueError, match="Country 'Unknown' not found in country codes."):
        task_func(data, date_format, country)

def test_task_func_invalid_input_types():
    data = [1, 2, 3]
    date_format = '%Y-%m-%d'
    country = 'Russia'
    with pytest.raises(ValueError, match="Invalid input types."):
        task_func(data, date_format, country)

def test_task_func_custom_country_codes():
    data = pd.DataFrame({'dates': ['2023-01-01', '2023-02-01', '2023-03-01']})
    date_format = '%Y-%m-%d'
    country = 'Custom'
    country_codes = {'Custom': 'custom_code'}
    ax = task_func(data, date_format, country, country_codes=country_codes)
    assert isinstance(ax, pd.plotting._matplotlib.hist.Plot)
    assert 'Date Distribution' in ax.get_title()
    assert 'Frequency' in ax.get_ylabel()