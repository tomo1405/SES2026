import pytest
from src_0847 import task_func

def test_task_func_empty_list():
    obj_list = []
    attr = 'attr'
    df = task_func(obj_list, attr)
    assert df.empty

def test_task_func_single_obj():
    obj_list = [{'attr': 'value'}]
    attr = 'attr'
    df = task_func(obj_list, attr)
    assert df.shape == (1, 2)
    assert df['attribute'][0] == 'value'
    assert df['count'][0] == 1

def test_task_func_multiple_objs():
    obj_list = [{'attr': 'value1'}, {'attr': 'value2'}, {'attr': 'value1'}]
    attr = 'attr'
    df = task_func(obj_list, attr)
    assert df.shape == (2, 2)
    assert df['attribute'][0] == 'value1'
    assert df['count'][0] == 2
    assert df['attribute'][1] == 'value2'
    assert df['count'][1] == 1

def test_task_func_invalid_attr():
    obj_list = [{'attr': 'value'}]
    attr = 'invalid_attr'
    with pytest.raises(AttributeError):
        task_func(obj_list, attr)