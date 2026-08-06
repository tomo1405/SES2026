import pytest
from src_0386 import task_func
from collections import Counter
import matplotlib.pyplot as plt

@pytest.fixture
def sample_fruit_dict():
    return {
        '1': 'Apple',
        '2': 'Banana',
        '3': 123,
        '4': 'Cherry',
        '5': 'Orange',
        '6': 'Apple',
        '7': 'Grape',
        '8': 'Honeydew',
        '9': 'Indian Prune',
        '10': 'Jackfruit'
    }

def test_task_func(sample_fruit_dict):
    expected_counter = Counter({
        'Apple': 2,
        'Banana': 1,
        'Cherry': 1,
        'Grape': 1,
        'Honeydew': 1,
        'Indian Prune': 1,
        'Jackfruit': 1
    })
    result_counter, ax = task_func(sample_fruit_dict)
    
    assert result_counter == expected_counter
    assert isinstance(ax, plt.Axes)

def test_task_func_no_valid_fruits():
    invalid_fruit_dict = {
        '1': 'Pineapple',
        '2': 'Watermelon',
        '3': 'Mango'
    }
    expected_counter = Counter()
    result_counter, ax = task_func(invalid_fruit_dict)
    
    assert result_counter == expected_counter
    assert isinstance(ax, plt.Axes)

def test_task_func_empty_dict():
    empty_dict = {}
    expected_counter = Counter()
    result_counter, ax = task_func(empty_dict)
    
    assert result_counter == expected_counter
    assert isinstance(ax, plt.Axes)