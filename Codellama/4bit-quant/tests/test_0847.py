import pandas as pd
from src_0847 import task_func


def test_task_func():
    obj_list = [
        {'name': 'John', 'age': 25},
        {'name': 'Jane', 'age': 30},
        {'name': 'Jim', 'age': 35},
    ]
    attr = 'name'
    expected_result = pd.DataFrame({'attribute': ['John', 'Jane', 'Jim'], 'count': [1, 1, 1]})
    result = task_func(obj_list, attr)
    assert result.equals(expected_result)

def test_task_func_empty_list():
    obj_list = []
    attr = 'name'
    expected_result = pd.DataFrame()
    result = task_func(obj_list, attr)
    assert result.equals(expected_result)

def test_task_func_invalid_attr():
    obj_list = [
        {'name': 'John', 'age': 25},
        {'name': 'Jane', 'age': 30},
        {'name': 'Jim', 'age': 35},
    ]
    attr = 'invalid_attr'
    expected_result = pd.DataFrame()
    result = task_func(obj_list, attr)
    assert result.equals(expected_result)