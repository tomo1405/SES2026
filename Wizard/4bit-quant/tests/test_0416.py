python
import pandas as pd
import codecs
import pytest

def task_func(dataframe: pd.DataFrame) -> pd.DataFrame:
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("The input must be a pandas DataFrame.")

    if 'UnicodeString' not in dataframe.columns:
        raise KeyError("'UnicodeString' column not found in the DataFrame.")

    dataframe['UnicodeString'] = dataframe['UnicodeString'].apply(lambda x: codecs.decode(x, 'unicode_escape'))

    return dataframe

def test_task_func():
    # Test case 1: Valid input
    df = pd.DataFrame({'UnicodeString': ['Hello, world!']})
    expected_df = pd.DataFrame({'UnicodeString': ['Hello, world!']})
    assert task_func(df).equals(expected_df)

    # Test case 2: Invalid input (not a DataFrame)
    with pytest.raises(TypeError):
        task_func('not a DataFrame')

    # Test case 3: Invalid input (missing UnicodeString column)
    df = pd.DataFrame({'not_UnicodeString': ['Hello, world!']})
    with pytest.raises(KeyError):
        task_func(df)

    # Test case 4: Invalid input (UnicodeString column has non-string values)
    df = pd.DataFrame({'UnicodeString': [1, 2, 3]})
    with pytest.raises(TypeError):
        task_func(df)