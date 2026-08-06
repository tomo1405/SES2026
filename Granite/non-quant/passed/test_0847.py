import pytest
from src_0847 import task_func
import pandas as pd
import collections

def test_task_func_with_empty_list():
    obj_list = []
    attr = 'some_attribute'
    expected_df = pd.DataFrame()
    actual_df = task_func(obj_list, attr)
    assert actual_df.equals(expected_df)

def test_task_func_with_non_empty_list():
    obj_list = [collections.Counter({'a': 1, 'b': 2}), collections.Counter({'a': 1, 'c': 3})]
    attr = 'most_common'
    expected_df = pd.DataFrame({'attribute': ['a', 'b', 'c'], 'count': [2, 1, 1]})
    actual_df = task_func(obj_list, attr)
    assert actual_df.equals(expected_df)

def test_task_func_with_invalid_attr():
    obj_list = [collections.Counter({'a': 1, 'b': 2}), collections.Counter({'a': 1, 'c': 3})]
    attr = 'invalid_attribute'
    with pytest.raises(AttributeError):
        task_func(obj_list, attr)