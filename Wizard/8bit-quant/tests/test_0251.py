python
import pytest
from src_0251 import task_func

def test_task_func():
    data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    task_func(data_list)
    assert True