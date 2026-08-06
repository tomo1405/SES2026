import pandas as pd
import pytest
from src_0743 import task_func


def test_task_func():
    list_of_pairs = [('cat1', 10), ('cat2', 20), ('cat3', 30)]
    expected_df = pd.DataFrame({
        'Category': ['cat1', 'cat2', 'cat3'],
        'Value': [0.0, 0.5, 1.0]
    })
    actual_df = task_func(list_of_pairs)
    pd.testing.assert_frame_equal(actual_df, expected_df)

def test_task_func_empty_input():
    with pytest.raises(Exception) as excinfo:
        task_func([])
    assert 'The input array should not be empty.' in str(excinfo.value)

def test_task_func_non_numeric_values():
    list_of_pairs = [('cat1', 'abc'), ('cat2', 20), ('cat3', 30)]
    with pytest.raises(ValueError) as excinfo:
        task_func(list_of_pairs)
    assert 'The values have to be numeric.' in str(excinfo.value)