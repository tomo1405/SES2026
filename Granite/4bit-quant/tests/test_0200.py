import pandas as pd
import pytz
from datetime import datetime
from random import randint, seed as set_seed
from src_0200 import task_func
import pytest

@pytest.mark.parametrize(
    "utc_datetime, expected_output",
    [
        (
            datetime(2023, 1, 1, 0, 0, 0, tzinfo=pytz.utc),
            pd.DataFrame(
                [
                    ['New York', '2023-01-01 00:00:00 UTC', 'Sunny'],
                    ['London', '2023-01-01 01:00:00 BST', 'Cloudy'],
                    ['Beijing', '2023-01-01 08:00:00 CST', 'Rainy'],
                    ['Tokyo', '2023-01-01 15:00:00 JST', 'Snowy'],
                    ['Sydney', '2023-01-01 10:00:00 AEDT', 'Stormy']
                ],
                columns=['City', 'Local Time', 'Weather Condition']
            )
        ),
        (
            datetime(2023, 1, 1, 12, 0, 0, tzinfo=pytz.utc),
            pd.DataFrame(
                [
                    ['New York', '2023-01-01 12:00:00 UTC', 'Sunny'],
                    ['London', '2023-01-01 13:00:00 BST', 'Cloudy'],
                    ['Beijing', '2023-01-01 20:00:00 CST', 'Rainy'],
                    ['Tokyo', '2023-01-01 21:00:00 JST', 'Snowy'],
                    ['Sydney', '2023-01-01 16:00:00 AEDT', 'Stormy']
                ],
                columns=['City', 'Local Time', 'Weather Condition']
            )
        )
    ]
)
def test_task_func(utc_datetime, expected_output):
    set_seed(42)
    report_df = task_func(utc_datetime)
    assert report_df.equals(expected_output)

def test_task_func_invalid_utc_datetime():
    with pytest.raises(ValueError) as exc_info:
        task_func(datetime(2023, 1, 1))
    assert "utc_datetime must be a datetime object with tzinfo set to UTC." in str(exc_info.value)

def test_task_func_invalid_city():
    with pytest.raises(ValueError) as exc_info:
        task_func(datetime(2023, 1, 1, 0, 0, 0, tzinfo=pytz.utc), cities=['Invalid City'])
    assert "Timezone for Invalid City not provided in timezones parameter." in str(exc_info.value)