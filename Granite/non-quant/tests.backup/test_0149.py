import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pytest

def task_func(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    le = LabelEncoder()
    df[column_name] = le.fit_transform(df[column_name])
    return df

def test_task_func():
    # Test case 1: Test with an empty DataFrame
    df = pd.DataFrame()
    column_name = 'column'
    expected_result = pd.DataFrame()
    result = task_func(df, column_name)
    assert result.equals(expected_result)

    # Test case 2: Test with a DataFrame containing a single column
    df = pd.DataFrame({'column': ['A', 'B', 'C']})
    column_name = 'column'
    expected_result = pd.DataFrame({'column': [0, 1, 2]})
    result = task_func(df, column_name)
    assert result.equals(expected_result)

    # Test case 3: Test with a DataFrame containing multiple columns
    df = pd.DataFrame({'column1': ['A', 'B', 'C'], 'column2': [1, 2, 3]})
    column_name = 'column1'
    expected_result = pd.DataFrame({'column1': [0, 1, 2], 'column2': [1, 2, 3]})
    result = task_func(df, column_name)
    assert result.equals(expected_result)

if __name__ == '__main__':
    pytest.main()