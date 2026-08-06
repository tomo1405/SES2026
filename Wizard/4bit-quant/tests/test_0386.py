python
import pytest
from src_0386 import task_func

def test_task_func():
    fruit_dict = {'A': 'Apple', 'B': 'Banana', 'C': 'Cherry', 'D': 'Date', 'E': 'Elderberry', 'F': 'Fig', 'G': 'Grape', 'H': 'Honeydew', 'I': 'Indian Prune', 'J': 'Jackfruit'}
    fruit_counter, ax = task_func(fruit_dict)
    assert fruit_counter == {'Apple': 1, 'Banana': 1, 'Cherry': 1, 'Date': 1, 'Elderberry': 1, 'Fig': 1, 'Grape': 1, 'Honeydew': 1, 'Indian Prune': 1, 'Jackfruit': 1}
    assert ax.get_xlabel() == 'Fruits'
    assert ax.get_ylabel() == 'Frequency'