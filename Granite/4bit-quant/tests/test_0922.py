import pytest
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(data, columns):
    df = pd.DataFrame(data)
    scaler = MinMaxScaler()
    df_copy = df.copy()
    df_copy[columns] = scaler.fit_transform(df_copy[columns])
    return df_copy

def test_task_func():
    data = [[1, 2], [3, 4], [5, 6]]
    columns = ['col1', 'col2']
    expected_result = [[0.0, 0.5], [0.5, 1.0], [1.0, 1.5]]
    result = task_func(data, columns)
    assert result.values.tolist() == expected_result
    assert result.shape == (3, 2)
    assert result.columns.tolist() == ['col1', 'col2']

def test_task_func_with_invalid_input():
    data = [[1, 2], [3, 4], [5, 6]]
    columns = ['col1', 'col3']
    with pytest.raises(ValueError):
        task_func(data, columns)