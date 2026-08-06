import pandas as pd
import pytest
from src_0847 import task_func


def test_task_func_empty_list():
    obj_list = []
    attr = 'attr'
    expected = pd.DataFrame()
    assert task_func(obj_list, attr).equals(expected)

def test_task_func_single_obj():
    obj_list = [{'attr': 'value'}]
    attr = 'attr'
    expected = pd.DataFrame({'attribute': ['value'], 'count': [1]})
    assert task_func(obj_list, attr).equals(expected)

def test_task_func_multiple_objs():
    obj_list = [{'attr': 'value1'}, {'attr': 'value2'}, {'attr': 'value1'}]
    attr = 'attr'
    expected = pd.DataFrame({'attribute': ['value1', 'value2'], 'count': [2, 1]})
    assert task_func(obj_list, attr).equals(expected)

def test_task_func_invalid_attr():
    obj_list = [{'attr': 'value'}]
    attr = 'invalid_attr'
    with pytest.raises(AttributeError):
        task_func(obj_list, attr)