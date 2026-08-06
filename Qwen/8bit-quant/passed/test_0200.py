import pytest
from src_0200 import task_func
import pandas as pd
from datetime import datetime, timezone

def test_task_func_invalid_utc_datetime():
    with pytest.raises(ValueError, match="utc_datetime must be a datetime object with tzinfo set to UTC."):
        task_func("2023-10-01T12:00:00Z")

def test_task_func_missing_timezone():
    with pytest.raises(ValueError, match="Timezone for Paris not provided in timezones parameter."):
        task_func(datetime.now(timezone.utc), cities=['Paris'])

def test_task_func_valid_input():
    utc_datetime = datetime.now(timezone.utc)
    df = task_func(utc_datetime)
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ['City', 'Local Time', 'Weather Condition']
    assert len(df) == 5  # Number of cities

def test_task_func_custom_cities_and_weather():
    cities = ['Los Angeles', 'Berlin']
    weather_conditions = ['Foggy', 'Windy']
    timezones = {
        'Los Angeles': 'America/Los_Angeles',
        'Berlin': 'Europe/Berlin'
    }
    df = task_func(datetime.now(timezone.utc), cities=cities, weather_conditions=weather_conditions, timezones=timezones)
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ['City', 'Local Time', 'Weather Condition']
    assert len(df) == 2  # Number of custom cities

def test_task_func_randomness():
    utc_datetime = datetime.now(timezone.utc)
    df1 = task_func(utc_datetime)
    df2 = task_func(utc_datetime)
    assert df1.equals(df2), "Randomness should be consistent with the same seed"

def test_task_func_seed_consistency():
    utc_datetime = datetime.now(timezone.utc)
    df1 = task_func(utc_datetime, seed=123)
    df2 = task_func(utc_datetime, seed=123)
    assert df1.equals(df2), "Same seed should produce the same output"