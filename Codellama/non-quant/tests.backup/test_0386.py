import pytest
from src_0386 import task_func

def test_task_func():
    fruit_dict = {'fruit1': 'Apple', 'fruit2': 'Banana', 'fruit3': 'Cherry', 'fruit4': 'Date', 'fruit5': 'Elderberry', 'fruit6': 'Fig', 'fruit7': 'Grape', 'fruit8': 'Honeydew', 'fruit9': 'Indian Prune', 'fruit10': 'Jackfruit'}
    expected_fruit_list = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape', 'Honeydew', 'Indian Prune', 'Jackfruit']
    expected_fruit_counter = Counter(expected_fruit_list)
    
    actual_fruit_counter, actual_axes = task_func(fruit_dict)
    
    assert actual_fruit_counter == expected_fruit_counter
    assert actual_axes.get_xlabel() == 'Fruit'
    assert actual_axes.get_ylabel() == 'Count'
    assert actual_axes.get_title() == 'Fruit Count'
    assert actual_axes.get_xticks() == expected_fruit_list
    assert actual_axes.get_yticks() == list(expected_fruit_counter.values())