import pandas as pd
import pytest
from src_1077 import task_func


@pytest.mark.parametrize("time_strings, target_tz, expected_df", [
    (["12/01/18 12:00:00.000", "12/01/18 12:00:00.000"], "UTC", pd.DataFrame({"Original Time": ["12/01/18 12:00:00.000", "12/01/18 12:00:00.000"], "Converted Time": ["12/01/18 12:00:00.000", "12/01/18 12:00:00.000"]})),
    (["12/01/18 12:00:00.000", "12/01/18 12:00:00.000"], "America/New_York", pd.DataFrame({"Original Time": ["12/01/18 12:00:00.000", "12/01/18 12:00:00.000"], "Converted Time": ["12/01/18 12:00:00.000", "12/01/18 12:00:00.000"]})),
    (["12/01/18 12:00:00.000", "12/01/18 12:00:00.000"], "Asia/Tokyo", pd.DataFrame({"Original Time": ["12/01/18 12:00:00.000", "12/01/18 12:00:00.000"], "Converted Time": ["12/01/18 12:00:00.000", "12/01/18 12:00:00.000"]})),
])
def test_task_func(time_strings, target_tz, expected_df):
    df = task_func(time_strings, target_tz)
    assert df.equals(expected_df)