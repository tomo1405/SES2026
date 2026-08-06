python
import pandas as pd
import pytest
from sklearn.preprocessing import LabelEncoder
from src_0224 import task_func

def test_task_func():
    # Test case 1: Valid input
    df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
    dct = {'a': 1, 'b': 2, 'c': 3}
    columns = ['B']
    expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': [1, 2, 3]})
    result_df = task_func(df, dct, columns)
    assert result_df.equals(expected_df)

    # Test case 2: Invalid input (df is not a DataFrame)
    df = 'not a DataFrame'
    dct = {'a': 1, 'b': 2, 'c': 3}
    columns = ['B']
    with pytest.raises(ValueError):
        task_func(df, dct, columns)

    # Test case 3: Invalid input (columns is not a list)
    df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
    dct = {'a': 1, 'b': 2, 'c': 3}
    columns = 'B'
    with pytest.raises(TypeError):
        task_func(df, dct, columns)

    # Test case 4: Invalid input (columns contains non-existent column)
    df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
    dct = {'a': 1, 'b': 2, 'c': 3}
    columns = ['C']
    with pytest.raises(KeyError):
        task_func(df, dct, columns)