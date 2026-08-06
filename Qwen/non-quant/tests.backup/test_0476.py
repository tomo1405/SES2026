import pytest
from src_0476 import task_func
import pandas as pd
from datetime import datetime

def test_task_func_invalid_input_types():
    with pytest.raises(ValueError, match="Invalid input types."):
        task_func([], "%Y-%m-%d", "Russia")

def test_task_func_country_not_in_codes():
    with pytest.raises(ValueError, match="Country 'Unknown' not found in country codes."):
        task_func(pd.DataFrame({'dates': ['2023-01-01']}), "%Y-%m-%d", "Unknown")

def test_task_func_date_format_mismatch():
    with pytest.raises(ValueError, match="Date format mismatch."):
        task_func(pd.DataFrame({'dates': ['01-01-2023']}), "%Y-%m-%d", "Russia")

def test_task_func_valid_data():
    data = pd.DataFrame({'dates': ['2023-01-01', '2023-01-02', '2023-01-01']})
    ax = task_func(data, "%Y-%m-%d", "Russia")
    assert 'parsed_dates' in data.columns
    assert all(isinstance(date, datetime.date) for date in data['parsed_dates'])
    assert ax.get_title() == 'Date Distribution'
    assert ax.get_ylabel() == 'Frequency'

def test_task_func_with_custom_country_codes():
    custom_country_codes = {'Russia': 'ru_RU', 'CustomLand': 'cl_CL'}
    data = pd.DataFrame({'dates': ['2023-01-01', '2023-01-02']})
    ax = task_func(data, "%Y-%m-%d", "CustomLand", country_codes=custom_country_codes)
    assert 'parsed_dates' in data.columns
    assert all(isinstance(date, datetime.date) for date in data['parsed_dates'])
    assert ax.get_title() == 'Date Distribution'
    assert ax.get_ylabel() == 'Frequency'