import pytest
from src_0569 import task_func

def test_task_func():
    f_list = [lambda x: x**2, lambda x, y: x*y, lambda x, y, z: x+y+z]
    df = task_func(f_list)
    assert df.shape == (3, 2)
    assert df.index.tolist() == ['<lambda>', '<lambda>', '<lambda>']
    assert df['Number of Arguments'].tolist() == [1, 2, 3]

def test_task_func_with_lambda():
    f_list = [lambda x: x**2, lambda x, y: x*y, lambda x, y, z: x+y+z]
    with pytest.raises(ValueError):
        task_func(f_list)