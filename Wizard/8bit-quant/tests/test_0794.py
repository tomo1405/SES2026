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

# Test the function
def test_task_func():
    # Test case 1
    assert task_func() == np.array(['E', 'F', 'G', 'A', 'B', 'C', 'D', 'H', 'I', 'J'])
    # Test case 2
    assert task_func(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']) == np.array(['E', 'F', 'G', 'A', 'B', 'C', 'D', 'H', 'I', 'J'])
    # Test case 3
    assert task_func(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']) == np.array(['E', 'F', 'G', 'A', 'B', 'C', 'D', 'H', 'I', 'J'])
    # Test case 4
    assert task_func(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']) == np.array(['E', 'F', 'G', 'A', 'B', 'C', 'D', 'H', 'I', 'J'])
    # Test case 5
    assert task_func(['A', 'B', 'C', 'D', 'E', 'F', 'G']) == np.array(['E', 'F', 'G', 'A', 'B', 'C', 'D', 'H', 'I', 'J'])
    # Test case 6
    assert task_func(['A', 'B', 'C', 'D', 'E', 'F']) == np.array(['E', 'F', 'G', 'A', 'B', 'C', 'D', 'H', 'I', 'J'])
    # Test case 7
    assert task_func(['A', 'B', 'C', 'D', 'E']) == np.array(['E', 'F', 'G', 'A', 'B', 'C', 'D', 'H', 'I', 'J'])
    # Test case 8
    assert task_func(['A', 'B', 'C', 'D']) == np.array(['E', 'F', 'G', 'A', 'B', 'C', 'D', 'H', 'I', 'J'])
    # Test case 9
    assert task_func(['A', 'B', 'C']) == np.array(['E', 'F', 'G', 'A', 'B', 'C', 'D', 'H', 'I', 'J'])
    # Test case 10
    assert task_func(['A', 'B']) == np.array(['E', 'F', 'G', 'A', 'B', 'C', 'D', 'H', 'I', 'J'])
    # Test case 11
    assert task_func(['A']) == np.array(['E', 'F', 'G', 'A', 'B', 'C', 'D', 'H', 'I', 'J'])
    # Test case 12
    assert task_func([]) == np.array(['E', 'F', 'G', 'A', 'B', 'C', 'D', 'H', 'I', 'J'])

# Run the tests
test_task_func()