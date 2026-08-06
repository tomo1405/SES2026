import pandas as pd
from src_1047 import task_func


def test_task_func():
    date_str = "2022-01-01"
    expected_df = pd.DataFrame({"Employee": ["John", "Alice", "Bob", "Charlie", "Dave"],
                               "Date": ["2022-01-01", "2022-01-02", "2022-01-03", "2022-01-04", "2022-01-05"]})
    actual_df = task_func(date_str)
    assert actual_df.equals(expected_df)