import pandas as pd
import matplotlib.pyplot as plt
import pytest

from src_1061 import task_func

@pytest.mark.parametrize(
    "df, column_name, expected_message, expected_ax_title",
    [
        (pd.DataFrame(), "column_name", "The DataFrame is empty or the specified column has no data.", "Distribution of values in column_name (No Data)"),
        (pd.DataFrame({"column_name": [1, 1, 1, 1, 1]}), "column_name", "The distribution of values is uniform.", "Distribution of values in column_name"),
        (pd.DataFrame({"column_name": [1, 2, 3, 4, 5]}), "column_name", "The distribution of values is not uniform.", "Distribution of values in column_name"),
    ],
)
def test_task_func(df, column_name, expected_message, expected_ax_title):
    message, ax = task_func(df, column_name)
    assert message == expected_message
    assert ax.get_title() == expected_ax_title