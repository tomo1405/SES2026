import re
import pandas as pd
import pytest
from src_0484 import task_func

@pytest.mark.parametrize(
    "df, column_name, pattern, expected",
    [
        (
            pd.DataFrame({"col1": ["Hello world", "Goodbye world"]}),
            "col1",
            r"world",
            pd.DataFrame({"col1": ["dlrow olleH", "dlrow olleG"]}),
        ),
        (
            pd.DataFrame({"col1": ["Hello world", "Goodbye world"]}),
            "col1",
            r"^w",
            pd.DataFrame({"col1": ["Hello dlrow", "Goodbye dlrow"]}),
        ),
        (
            pd.DataFrame({"col1": ["Hello world", "Goodbye world"]}),
            "col2",
            r"world",
            pd.DataFrame({"col1": ["Hello world", "Goodbye world"]}),
        ),
    ],
)
def test_task_func(df, column_name, pattern, expected):
    result = task_func(df, column_name, pattern)
    assert result.equals(expected)