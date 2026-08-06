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
    assert df.equals(pd.DataFrame([('a', 1), ('b', 2), ('c', 3)], columns=['Category', 'Value']))