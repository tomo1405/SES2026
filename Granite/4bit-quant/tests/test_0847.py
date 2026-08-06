import pytest
from src_0847 import task_func

def test_task_func():
    obj_list = [object() for _ in range(10)]
    attr = 'attr'
    df = task_func(obj_list, attr)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (len(set(getattr(obj, attr) for obj in obj_list)), 2)
    assert list(df.columns) == ['attribute', 'count']