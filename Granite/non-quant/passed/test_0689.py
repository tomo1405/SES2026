import pandas as pd
from sklearn.preprocessing import StandardScaler
import pytest

def task_func(df):
    scaler = StandardScaler()
    df_standardized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    return df_standardized

def test_task_func():
    # Test case 1: Test with a dataframe containing all numerical values
    df = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['A', 'B'])
    expected_result = pd.DataFrame([[-1.22474487, -1.22474487], [0, 0], [1.22474487, 1.22474487]], columns=['A', 'B'])
    result = task_func(df)
    assert result.equals(expected_result)

    # Test case 2: Test with a dataframe containing categorical values
    df = pd.DataFrame([['cat', 'dog'], ['dog', 'cat'], ['cat', 'dog']], columns=['A', 'B'])
    with pytest.raises(ValueError):
        task_func(df)