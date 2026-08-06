python
import pytest
from datetime import datetime
import pandas as pd
try:
    from zoneinfo import ZoneInfo
except ImportError:
    from pytz import timezone as ZoneInfo

TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"

def task_func(time_strings, target_tz):
    data = []

    for time_string in time_strings:
        utc_time = datetime.strptime(time_string, TIME_FORMAT)
        converted_time = utc_time.replace(tzinfo=ZoneInfo("UTC")).astimezone(
            ZoneInfo(target_tz)
        )
        data.append([time_string, converted_time.strftime(TIME_FORMAT)])

    df = pd.DataFrame(data, columns=["Original Time", "Converted Time"])
    return df

def test_task_func():
    time_strings = ["01/01/1970 00:00:00.000000", "01/01/1970 00:00:00.000001"]
    target_tz = "US/Pacific"
    expected_df = pd.DataFrame(
        [
            ["01/01/1970 00:00:00.000000", "01/01/1970 08:00:00.000000"],
            ["01/01/1970 00:00:00.000001", "01/01/1970 08:00:00.000001"],
        ],
        columns=["Original Time", "Converted Time"],
    )
    actual_df = task_func(time_strings, target_tz)
    assert actual_df.equals(expected_df)