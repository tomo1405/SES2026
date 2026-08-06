import pytest
from src_0743 import task_func

def test_task_func_empty_list():
    with pytest.raises(Exception):
        task_func([])

def test_task_func_non_numeric_values():
    with pytest.raises(ValueError):
        task_func([('a', 1), ('b', 2)])

def test_task_func_valid_input():
    df = task_func([('a', 1), ('b', 2), ('c', 3)])
    assert df.shape == (3, 2)
    assert df.columns.tolist() == ['Category', 'Value']
    assert df.dtypes.tolist() == ['object', 'float64']
    assert df.Value.min() == 0
    assert df.Value.max() == 1