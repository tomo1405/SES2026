import numpy as np
from src_0030 import task_func


def test_task_func():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    expected_output = 'AXwBAAIAAAA='
    
    output = task_func(data)
    
    assert output == expected_output