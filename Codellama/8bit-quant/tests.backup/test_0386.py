import pytest
from src_0386 import task_func

def test_task_func():
    fruit_dict = {'fruit1': 'Apple', 'fruit2': 'Banana', 'fruit3': 'Cherry', 'fruit4': 'Date', 'fruit5': 'Elderberry', 'fruit6': 'Fig', 'fruit7': 'Grape', 'fruit8': 'Honeydew', 'fruit9': 'Indian Prune', 'fruit10': 'Jackfruit'}
    expected_fruit_counter = Counter({'Apple': 1, 'Banana': 1, 'Cherry': 1, 'Date': 1, 'Elderberry': 1, 'Fig': 1, 'Grape': 1, 'Honeydew': 1, 'Indian Prune': 1, 'Jackfruit': 1})
    expected_plt_gca = plt.gca()

    fruit_counter, plt_gca = task_func(fruit_dict)

    assert fruit_counter == expected_fruit_counter
    assert plt_gca == expected_plt_gca