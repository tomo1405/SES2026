import pytest
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(list_of_pairs):
    if len(list_of_pairs) == 0:
        raise Exception('The input array should not be empty.')

    df = pd.DataFrame(list_of_pairs, columns=['Category', 'Value'])

    if pd.api.types.is_numeric_dtype(df.Value) is not True:
        raise ValueError('The values have to be numeric.')

    scaler = MinMaxScaler()
    df['Value'] = scaler.fit_transform(df[['Value']])

    return df

def test_task_func():
    list_of_pairs = [('cat1', 10), ('cat2', 20), ('cat3', 30)]
    expected_df = pd.DataFrame({
        'Category': ['cat1', 'cat2', 'cat3'],
        'Value': [0.0, 0.5, 1.0]
    })
    actual_df = task_func(list_of_pairs)
    pd.testing.assert_frame_equal(actual_df, expected_df)

def test_task_func_with_empty_list():
    with pytest.raises(Exception) as excinfo:
        task_func([])
    assert 'The input array should not be empty.' in str(excinfo.value)

def test_task_func_with_non_numeric_values():
    list_of_pairs = [('cat1', 'abc'), ('cat2', 20), ('cat3', 30)]
    with pytest.raises(ValueError) as excinfo:
        task_func(list_of_pairs)
    assert 'The values have to be numeric.' in str(excinfo.value)