import pytest
from src_1077 import task_func

def test_task_func():
    time_strings = ["01/01/22 00:00:00.000000", "01/02/22 12:00:00.000000"]
    target_tz = "America/New_York"
    expected_df = pd.DataFrame(
        data=[
            ["01/01/22 00:00:00.000000", "01/01/22 05:00:00.000000"],
            ["01/02/22 12:00:00.000000", "01/02/22 18:00:00.000000"],
        ],
        columns=["Original Time", "Converted Time"],
    )
    actual_df = task_func(time_strings, target_tz)
    assert actual_df.equals(expected_df)