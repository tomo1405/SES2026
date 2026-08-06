import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from src_0743 import task_func
import pytest

@pytest.fixture
def list_of_pairs():
    return [('cat1', 10), ('cat2', 20), ('cat3', 30)]

def test_task_func_with_valid_input(list_of_pairs):
    df = task_func(list_of_pairs)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 2)
    assert df.columns.tolist() == ['Category', 'Value']

def test_task_func_with_empty_input():
    with pytest.raises(Exception) as exc_info:
        task_func([])
    assert 'The input array should not be empty.' in str(exc_info.value)

def test_task_func_with_non_numeric_values(list_of_pairs):
    list_of_pairs.append(('cat4', 'abc'))
    with pytest.raises(ValueError) as exc_info:
        task_func(list_of_pairs)
    assert 'The values have to be numeric.' in str(exc_info.value)