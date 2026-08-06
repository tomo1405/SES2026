import pandas as pd
from src_1077 import task_func


def test_task_func():
    time_strings = ["12/01/20 12:00:00.000", "12/01/20 13:00:00.000", "12/01/20 14:00:00.000"]
    target_tz = "America/New_York"
    expected_df = pd.DataFrame(
        {
            "Original Time": ["12/01/20 12:00:00.000", "12/01/20 13:00:00.000", "12/01/20 14:00:00.000"],
            "Converted Time": ["12/01/20 08:00:00.000", "12/01/20 09:00:00.000", "12/01/20 10:00:00.000"],
        }
    )
    actual_df = task_func(time_strings, target_tz)
    assert actual_df.equals(expected_df)