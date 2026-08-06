import pytest
from src_1077 import task_func

def test_task_func():
    # Test with a single time string
    time_strings = ["01/01/22 12:00:00.000000"]
    target_tz = "America/New_York"
    result_df = task_func(time_strings, target_tz)
    expected_data = [
        ["01/01/22 12:00:00.000000", "31/12/21 19:00:00.000000"]  # Example conversion
    ]
    expected_df = pd.DataFrame(expected_data, columns=["Original Time", "Converted Time"])
    assert result_df.equals(expected_df)

    # Test with multiple time strings
    time_strings = [
        "01/01/22 12:00:00.000000",
        "02/01/22 13:00:00.000000"
    ]
    target_tz = "Europe/London"
    result_df = task_func(time_strings, target_tz)
    expected_data = [
        ["01/01/22 12:00:00.000000", "01/01/22 12:00:00.000000"],  # Example conversion
        ["02/01/22 13:00:00.000000", "02/01/22 13:00:00.000000"]  # Example conversion
    ]
    expected_df = pd.DataFrame(expected_data, columns=["Original Time", "Converted Time"])
    assert result_df.equals(expected_df)

    # Test with invalid time format
    time_strings = ["01-01-22 12:00:00.000000"]
    target_tz = "Asia/Tokyo"
    with pytest.raises(ValueError):
        task_func(time_strings, target_tz)

    # Test with invalid timezone
    time_strings = ["01/01/22 12:00:00.000000"]
    target_tz = "Invalid/Timezone"
    with pytest.raises(pytz.UnknownTimeZoneError):
        task_func(time_strings, target_tz)

    # Test with empty list of time strings
    time_strings = []
    target_tz = "Europe/Berlin"
    result_df = task_func(time_strings, target_tz)
    expected_df = pd.DataFrame(columns=["Original Time", "Converted Time"])
    assert result_df.equals(expected_df)