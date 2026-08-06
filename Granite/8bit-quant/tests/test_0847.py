import pandas as pd
from src_0847 import task_func


def test_task_func():
    obj_list = [object() for _ in range(10)]
    attr = 'attr'
    df = task_func(obj_list, attr)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (0, 2)

def test_task_func_with_data():
    class MyObject:
        def __init__(self, attr):
            self.attr = attr
    obj_list = [MyObject(attr) for attr in ['a', 'b', 'a', 'c', 'a']]
    attr = 'attr'
    df = task_func(obj_list, attr)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 2)
    assert df.loc['a', 'count'] == 3
    assert df.loc['b', 'count'] == 1
    assert df.loc['c', 'count'] == 1