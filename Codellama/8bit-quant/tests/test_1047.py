from datetime import datetime

import pandas as pd
from src_1047 import task_func


def test_task_func():
    date_str = "2022-01-01"
    expected_df = pd.DataFrame({
        "Employee": ["John", "Alice", "Bob", "Charlie", "Dave"],
        "Date": [
            datetime(2022, 1, 1),
            datetime(2022, 1, 2),
            datetime(2022, 1, 3),
            datetime(2022, 1, 4),
            datetime(2022, 1, 5),
            datetime(2022, 1, 6),
            datetime(2022, 1, 7),
            datetime(2022, 1, 8),
            datetime(2022, 1, 9),
            datetime(2022, 1, 10)
        ]
    })

    actual_df = task_func(date_str)

    assert actual_df.equals(expected_df)