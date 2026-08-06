import matplotlib
import pandas as pd
import pytest
from src_0602 import task_func


def test_task_func():
    # Test case 1: Validate if 'Word' column exists in df
    df_invalid = pd.DataFrame({'Letter': ['A', 'B', 'C']})
    with pytest.raises(ValueError) as exc_info:
        task_func(df_invalid, 'A')
    assert "The DataFrame should contain a 'Word' column." in str(exc_info.value)

    # Test case 2: Handle empty DataFrame
    df_empty = pd.DataFrame()
    with pytest.warns(UserWarning) as record:
        result = task_func(df_empty, 'A')
    assert "The DataFrame is empty." in record[0].message.args[0]
    assert result is None

    # Test case 3: Filter df based on letter
    df_filtered = pd.DataFrame({'Word': ['Apple', 'Banana', 'Orange']})
    result = task_func(df_filtered, 'B')
    assert isinstance(result, matplotlib.axes.Axes)
    assert result.get_title() == "Word Lengths Distribution for Words Starting with 'B'"

    # Test case 4: Handle empty filtered df
    df_filtered_empty = pd.DataFrame({'Word': ['Cherry', 'Durian']})
    with pytest.warns(UserWarning) as record:
        result = task_func(df_filtered_empty, 'D')
    assert "No words start with the letter 'D'." in record[0].message.args[0]
    assert result is None