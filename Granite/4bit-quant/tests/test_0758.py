import numpy as np
from src_0758 import task_func


def test_task_func():
    arr = np.array(['1.2.3.4', '5.6.7.8', '9.10.11.12'])
    expected_output = np.array(['4.3.2.1', '8.7.6.5', '12.11.10.9'])
    
    output = task_func(arr)
    
    assert np.array_equal(output, expected_output)