import pytest
from src_0569 import task_func

def test_task_func_with_valid_functions():
    f_list = [
        lambda x: x**2,
        lambda x, y: x + y,
        lambda x, y, z: x * y * z
    ]
    df = task_func(f_list)
    assert df.shape == (3, 2)
    assert df.iloc[0, 0] == 'lambda'
    assert df.iloc[0, 1] == 1
    assert df.iloc[1, 0] == 'lambda'
    assert df.iloc[1, 1] == 2
    assert df.iloc[2, 0] == 'lambda'
    assert df.iloc[2, 1] == 3

def test_task_func_with_invalid_functions():
    f_list = [
        lambda x: x**2,
        lambda x, y: x + y,
        lambda x, y, z: x * y * z,
        lambda: 1
    ]
    with pytest.raises(ValueError):
        task_func(f_list)