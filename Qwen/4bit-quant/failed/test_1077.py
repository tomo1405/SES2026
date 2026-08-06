import pytest
from src_1077 import task_func

@pytest.fixture
def time_strings():
    return [
        "25/12/21 15:30:45.123456",
        "01/01/22 00:00:00.000000",
        "31/10/21 23:59:59.999999"
    ]

def test_task_func_with_valid_timezone(time_strings):
    target_tz = "America/New_York"
    result_df = task_func(time_strings, target_tz)
    
    assert isinstance(result_df, pd.DataFrame)
    assert len(result_df) == len(time_strings)
    assert all(col in result_df.columns for col in ["Original Time", "Converted Time"])

def test_task_func_with_invalid_timezone(time_strings):
    target_tz = "Invalid/Timezone"
    with pytest.raises(pytz.UnknownTimeZoneError):
        task_func(time_strings, target_tz)

def test_task_func_with_empty_input():
    target_tz = "Europe/London"
    result_df = task_func([], target_tz)
    
    assert isinstance(result_df, pd.DataFrame)
    assert result_df.empty

def test_task_func_with_single_time(time_strings):
    target_tz = "Asia/Tokyo"
    result_df = task_func(time_strings[:1], target_tz)
    
    assert isinstance(result_df, pd.DataFrame)
    assert len(result_df) == 1
    assert all(col in result_df.columns for col in ["Original Time", "Converted Time"])