import pandas as pd
import pytest
from src_1077 import task_func


def test_task_func():
    time_strings = ["01/01/22 12:00:00.000000", "02/01/22 13:00:00.000000"]
    target_tz = "US/Eastern"
    expected_df = pd.DataFrame(
        [
            ["01/01/22 12:00:00.000000", "01/01/22 07:00:00.000000"],
            ["02/01/22 13:00:00.000000", "02/01/22 08:00:00.000000"],
        ],
        columns=["Original Time", "Converted Time"],
    )
    df = task_func(time_strings, target_tz)
    assert df.equals(expected_df)

if __name__ == "__main__":
    pytest.main()