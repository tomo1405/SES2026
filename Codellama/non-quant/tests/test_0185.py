import pandas as pd
import pytest
from src_0185 import task_func


def test_task_func():
    # Test case 1: Test that the function returns a DataFrame with the correct column names
    dataframe = pd.DataFrame({'text': ['This is a sample text']})
    text_column = 'text'
    expected_columns = ['this', 'is', 'a', 'sample', 'text']
    result = task_func(dataframe, text_column)
    assert isinstance(result, pd.DataFrame)
    assert list(result.columns) == expected_columns

    # Test case 2: Test that the function returns a DataFrame with the correct data
    dataframe = pd.DataFrame({'text': ['This is a sample text']})
    text_column = 'text'
    expected_data = [[1, 1, 1, 1, 1]]
    result = task_func(dataframe, text_column)
    assert isinstance(result, pd.DataFrame)
    assert result.values.tolist() == expected_data

    # Test case 3: Test that the function raises a ValueError if the input is not a DataFrame
    dataframe = 'This is a sample text'
    text_column = 'text'
    with pytest.raises(ValueError):
        task_func(dataframe, text_column)

    # Test case 4: Test that the function raises a ValueError if the input column is not a string
    dataframe = pd.DataFrame({'text': ['This is a sample text']})
    text_column = 1
    with pytest.raises(ValueError):
        task_func(dataframe, text_column)

    # Test case 5: Test that the function raises a ValueError if the input column does not exist in the DataFrame
    dataframe = pd.DataFrame({'text': ['This is a sample text']})
    text_column = 'not_a_column'
    with pytest.raises(ValueError):
        task_func(dataframe, text_column)