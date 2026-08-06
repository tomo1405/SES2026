python
import pytest
from src_0386 import task_func

def test_task_func():
    fruit_dict = {'John': 'Apple', 'Mary': 'Banana', 'Tom': 'Cherry', 'David': 'Date', 'Emily': 'Elderberry', 'Jane': 'Fig', 'Lisa': 'Grape', 'Peter': 'Honeydew', 'Robert': 'Indian Prune', 'Sarah': 'Jackfruit'}
    fruit_counter, ax = task_func(fruit_dict)
    assert fruit_counter == {'Apple': 1, 'Banana': 1, 'Cherry': 1, 'Date': 1, 'Elderberry': 1, 'Fig': 1, 'Grape': 1, 'Honeydew': 1, 'Indian Prune': 1, 'Jackfruit': 1}
    assert ax.get_xlabel() == 'Fruits'
    assert ax.get_ylabel() == 'Frequency'