import pytest
from src_0569 import task_func

def test_task_func():
    f_list = [lambda x: x**2, lambda x, y: x*y, lambda x, y, z: x+y+z]
    df = task_func(f_list)
    assert df.equals(pd.DataFrame({'Function Name': ['<lambda>', '<lambda>', '<lambda>'],
                                  'Number of Arguments': [1, 2, 3]},
                                 index=['<lambda>', '<lambda>', '<lambda>']))

def test_task_func_invalid_input():
    f_list = [lambda x: x**2, lambda x, y: x*y, lambda x, y, z: x+y+z]
    with pytest.raises(ValueError):
        task_func(f_list, invalid_input=True)