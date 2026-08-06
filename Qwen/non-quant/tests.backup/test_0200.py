import pytest
from src_0200 import task_func
import pandas as pd
from datetime import datetime, timezone

def test_task_func_with_valid_input():
    utc_datetime = datetime(2023, 10, 1, 12, 0, 0, tzinfo=timezone.utc)
    result_df = task_func(utc_datetime)
    
    assert isinstance(result_df, pd.DataFrame)
    assert len(result_df) == 5
    assert all(col in result_df.columns for col in ['City', 'Local Time', 'Weather Condition'])
    
    expected_cities = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']
    assert all(city in result_df['City'].values for city in expected_cities)

def test_task_func_with_invalid_utc_datetime_type():
    with pytest.raises(ValueError, match="utc_datetime must be a datetime object with tzinfo set to UTC."):
        task_func("2023-10-01 12:00:00")

def test_task_func_with_missing_timezone():
    utc_datetime = datetime(2023, 10, 1, 12, 0, 0, tzinfo=timezone.utc)
    with pytest.raises(ValueError, match="Timezone for Paris not provided in timezones parameter."):
        task_func(utc_datetime, cities=['New York', 'Paris'])

def test_task_func_with_empty_cities_list():
    utc_datetime = datetime(2023, 10, 1, 12, 0, 0, tzinfo=timezone.utc)
    result_df = task_func(utc_datetime, cities=[])
    
    assert isinstance(result_df, pd.DataFrame)
    assert result_df.empty

def test_task_func_with_custom_seed():
    utc_datetime = datetime(2023, 10, 1, 12, 0, 0, tzinfo=timezone.utc)
    result_df_1 = task_func(utc_datetime, seed=123)
    result_df_2 = task_func(utc_datetime, seed=123)
    
    assert result_df_1.equals(result_df_2)