import pytest
from src_0386 import task_func

def test_task_func():
    fruit_dict = {'a': 'Apple', 'b': 'Banana', 'c': 'Cherry', 'd': 'Date', 'e': 'Elderberry', 'f': 'Fig', 'g': 'Grape', 'h': 'Honeydew', 'i': 'Indian Prune', 'j': 'Jackfruit'}
    expected_counter = Counter(['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape', 'Honeydew', 'Indian Prune', 'Jackfruit'])
    expected_ax = None  # You can replace this with the expected value of plt.gca()
    
    actual_counter, actual_ax = task_func(fruit_dict)
    
    assert actual_counter == expected_counter
    assert actual_ax == expected_ax