python
import numpy as np
import datetime
import pytest

def task_func(arr):
    vectorized_reverse = np.vectorize(lambda s: '.'.join(s.split('.')[::-1]))
    
    now = datetime.datetime.now()
    
    return vectorized_reverse(arr)

def test_task_func():
    arr = ['1.2.3.4', '5.6.7.8', '9.10.11.12']
    expected_result = ['4.3.2.1', '8.7.6.5', '12.11.10.9']
    result = task_func(arr)
    assert result == expected_result