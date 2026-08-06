python
import pickle
import os

# Constants
FILE_NAME = 'save.pkl'

def task_func(dt):
    with open(FILE_NAME, 'wb') as file:
        pickle.dump(dt, file)
    
    with open(FILE_NAME, 'rb') as file:
        loaded_dt = pickle.load(file)

    os.remove(FILE_NAME)

    return loaded_dt

# Test the function
def test_task_func():
    # Test case 1
    dt = {'a': 1, 'b': 2}
    expected_result = {'a': 1, 'b': 2}
    assert task_func(dt) == expected_result

    # Test case 2
    dt = {'c': 3, 'd': 4}
    expected_result = {'c': 3, 'd': 4}
    assert task_func(dt) == expected_result

    # Test case 3
    dt = {'e': 5, 'f': 6}
    expected_result = {'e': 5, 'f': 6}
    assert task_func(dt) == expected_result

# Run the tests
test_task_func()