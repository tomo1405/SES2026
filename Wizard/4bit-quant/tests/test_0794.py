python
import numpy as np
import random

# Constants
ELEMENTS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

def task_func(l=None):
    if l is None:
        l = ELEMENTS.copy()  # Use a copy to avoid modifying the original list
    random.shuffle(l)
    arr = np.array(l)
    arr = np.concatenate((arr[3:], arr[:3]))
    return arr

def test_task_func():
    # Test case 1: Test with default input
    assert task_func() == np.array(['E', 'F', 'G', 'A', 'B', 'C', 'D', 'H', 'I', 'J'])
    
    # Test case 2: Test with custom input
    assert task_func(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']) == np.array(['E', 'F', 'G', 'A', 'B', 'C', 'D', 'H', 'I', 'J'])
    
    # Test case 3: Test with empty input
    assert task_func([]) == np.array([])
    
    # Test case 4: Test with invalid input
    try:
        task_func('invalid input')
    except TypeError:
        assert True
    else:
        assert False