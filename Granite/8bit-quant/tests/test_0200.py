import pandas as pd
import pytz
from datetime import datetime
from random import randint, seed as set_seed
from src_0200 import task_func
import pytest

@pytest.fixture
def setup():
    set_seed(42)
    utc_datetime = datetime.now(pytz.utc)
    return utc_datetime

def test_task_func_valid_input(setup):
    utc_datetime = setup
    report_df = task_func(utc_datetime)
    assert isinstance(report_df, pd.DataFrame)

def test_task_func_invalid_input(setup):
    utc_datetime = setup
    with pytest.raises(ValueError):
        task_func(utc_datetime.strftime('%Y-%m-%d %H:%M:%S %Z'))

def test_task_func_city_not_in_timezones(setup):
    utc_datetime = setup
    with pytest.raises(ValueError):
        task_func(utc_datetime, cities=['New York', 'Invalid City'])

def test_task_func_weather_conditions(setup):
    utc_datetime = setup
    report_df = task_func(utc_datetime)
    weather_conditions = report_df['Weather Condition'].unique()
    assert all(condition in weather_conditions for condition in ['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Stormy'])