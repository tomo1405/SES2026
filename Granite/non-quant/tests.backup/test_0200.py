import pandas as pd
import pytz
from datetime import datetime
from random import randint, seed as set_seed
from src_0200 import task_func
import pytest

@pytest.fixture
def setup():
    set_seed(42)
    utc_datetime = datetime(2023, 5, 1, 12, 0, 0, tzinfo=pytz.utc)
    return utc_datetime

def test_task_func_valid_input(setup):
    utc_datetime = setup
    report_df = task_func(utc_datetime)
    assert isinstance(report_df, pd.DataFrame)

def test_task_func_invalid_input(setup):
    utc_datetime = setup
    with pytest.raises(ValueError):
        task_func(utc_datetime.replace(tzinfo=None))

def test_task_func_invalid_city(setup):
    utc_datetime = setup
    with pytest.raises(ValueError):
        task_func(utc_datetime, cities=['Invalid City'])

def test_task_func_invalid_weather_condition(setup):
    utc_datetime = setup
    with pytest.raises(ValueError):
        task_func(utc_datetime, weather_conditions=['Invalid Weather'])

def test_task_func_invalid_timezone(setup):
    utc_datetime = setup
    with pytest.raises(ValueError):
        task_func(utc_datetime, timezones={'Invalid City': 'Invalid Timezone'})