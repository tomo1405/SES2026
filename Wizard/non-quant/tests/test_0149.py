python
import pandas as pd
import pytest
from sklearn.preprocessing import LabelEncoder
from src_0149 import task_func

def test_task_func():
    # Test case 1: Test with a valid input
    df = pd.DataFrame({'column_name': ['a', 'b', 'c']})
    expected_df = pd.DataFrame({'column_name': [0, 1, 2]})
    assert task_func(df, 'column_name').equals(expected_df)

    # Test case 2: Test with a missing column
    df = pd.DataFrame({'column_name': ['a', 'b', 'c']})
    with pytest.raises(KeyError):
        task_func(df, 'missing_column')

    # Test case 3: Test with a non-string column
    df = pd.DataFrame({'column_name': [1, 2, 3]})
    with pytest.raises(TypeError):
        task_func(df, 'column_name')