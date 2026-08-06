from io import StringIO

import pandas as pd
from src_0171 import task_func


def test_task_func():
    csv_url = "https://raw.githubusercontent.com/pytest-dev/pytest/main/tests/test_data/test_data.csv"
    sort_by_column = "title"
    expected_df = pd.read_csv(StringIO(csv_data))
    expected_df = expected_df.sort_values(by=sort_by_column)
    actual_df = task_func(csv_url, sort_by_column)
    assert actual_df.equals(expected_df)