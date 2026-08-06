import pytest
from src_0200 import task_func
import pandas as pd
from datetime import datetime, timezone

def test_task_func_with_valid_input():
    utc_datetime = datetime(2023, 10, 1, 12, 0, 0, tzinfo=timezone.utc)
    expected_cities = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']
    expected_columns = ['City', 'Local Time', 'Weather Condition']
    
    result_df = task_func(utc_datetime)
    
    assert isinstance(result_df, pd.DataFrame)
    assert all(col in result_df.columns for col in expected_columns)
    assert all(city in result_df['City'].values for city in expected_cities)

def test_task_func_with_invalid_utc_datetime():
    utc_datetime = datetime(2023, 10, 1, 12, 0, 0)
    with pytest.raises(ValueError, match="utc_datetime must be a datetime object with tzinfo set to UTC."):
        task_func(utc_datetime)

def test_task_func_with_missing_timezone():
    utc_datetime = datetime(2023, 10, 1, 12, 0, 0, tzinfo=timezone.utc)
    cities = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney', 'Unknown City']
    with pytest.raises(ValueError, match="Timezone for Unknown City not provided in timezones parameter."):
        task_func(utc_datetime, cities=cities)

def test_task_func_with_custom_timezones_and_weather():
    utc_datetime = datetime(2023, 10, 1, 12, 0, 0, tzinfo=timezone.utc)
    cities = ['Paris', 'Berlin']
    timezones = {
        'Paris': 'Europe/Paris',
        'Berlin': 'Europe/Berlin'
    }
    weather_conditions = ['Windy', 'Foggy']
    
    result_df = task_func(utc_datetime, cities=cities, timezones=timezones, weather_conditions=weather_conditions)
    
    assert all(city in result_df['City'].values for city in cities)
    assert all(weather in weather_conditions for weather in result_df['Weather Condition'].values)