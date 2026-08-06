import pandas as pd
import pytest
from src_0054 import task_func


def test_task_func():
    text = "Name: John, Email: john@example.com, Age: 30, Country: US\nName: Jane, Email: jane@example.com, Age: 25, Country: UK"
    expected_df = pd.DataFrame([["John", "john@example.com", 30, "US"], ["Jane", "jane@example.com", 25, "UK"]], columns=COLUMN_NAMES)
    df = task_func(text)
    assert df.equals(expected_df)

def test_task_func_with_invalid_text():
    text = "Invalid text"
    with pytest.raises(Exception) as excinfo:
        task_func(text)
    assert "Invalid input" in str(excinfo.value)