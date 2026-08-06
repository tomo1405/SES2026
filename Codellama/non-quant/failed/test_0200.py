import pytest
from src_0200 import task_func

def test_task_func_utc_datetime_not_datetime():
    with pytest.raises(ValueError):
        task_func(utc_datetime='2022-01-01 12:00:00')

def test_task_func_utc_datetime_tzinfo_not_utc():
    with pytest.raises(ValueError):
        task_func(utc_datetime=datetime.now())

def test_task_func_cities_not_list():
    with pytest.raises(ValueError):
        task_func(utc_datetime=datetime.now(tz=pytz.utc), cities='New York')

def test_task_func_weather_conditions_not_list():
    with pytest.raises(ValueError):
        task_func(utc_datetime=datetime.now(tz=pytz.utc), weather_conditions='Sunny')

def test_task_func_timezones_not_dict():
    with pytest.raises(ValueError):
        task_func(utc_datetime=datetime.now(tz=pytz.utc), timezones='America/New_York')

def test_task_func_seed_not_int():
    with pytest.raises(ValueError):
        task_func(utc_datetime=datetime.now(tz=pytz.utc), seed='42')

def test_task_func_valid_input():
    report_df = task_func(utc_datetime=datetime.now(tz=pytz.utc), cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney'], weather_conditions=['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Stormy'], timezones={'New York': 'America/New_York', 'London': 'Europe/London', 'Beijing': 'Asia/Shanghai', 'Tokyo': 'Asia/Tokyo', 'Sydney': 'Australia/Sydney'}, seed=42)
    assert isinstance(report_df, pd.DataFrame)
    assert report_df.shape == (5, 3)
    assert report_df.columns.tolist() == ['City', 'Local Time', 'Weather Condition']
    assert report_df['City'].tolist() == ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']
    assert report_df['Local Time'].tolist() == ['2022-01-01 12:00:00 EST', '2022-01-01 17:00:00 GMT', '2022-01-01 08:00:00 CST', '2022-01-01 13:00:00 JST', '2022-01-01 16:00:00 AEST']
    assert report_df['Weather Condition'].tolist() == ['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Stormy']