import pandas as pd
from src_1077 import task_func


def test_task_func():
    time_strings = ["10/10/20 10:10:10.123456", "11/11/20 11:11:11.123456"]
    target_tz = "America/New_York"
    expected_df = pd.DataFrame(
        {
            "Original Time": ["10/10/20 10:10:10.123456", "11/11/20 11:11:11.123456"],
            "Converted Time": ["05/10/20 05:10:10.123456", "06/11/20 06:11:11.123456"],
        }
    )
    actual_df = task_func(time_strings, target_tz)
    assert actual_df.equals(expected_df)