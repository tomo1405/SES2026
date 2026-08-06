python
import numpy as np
import datetime

def task_func(arr):
    vectorized_reverse = np.vectorize(lambda s: '.'.join(s.split('.')[::-1]))
    
    now = datetime.datetime.now()
    
    return vectorized_reverse(arr)

def test_task_func():
    arr = np.array(['1.2.3.4', '5.6.7.8', '9.10.11.12'])
    expected_result = np.array(['4.3.2.1', '8.7.6.5', '12.11.10.9'])
    assert np.array_equal(task_func(arr), expected_result)