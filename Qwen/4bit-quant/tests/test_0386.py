from collections import Counter

from src_0386 import task_func


def test_task_func_with_valid_fruits():
    fruit_dict = {
        'a': 'Apple',
        'b': 'Banana',
        'c': 'Cherry',
        'd': 'Date',
        'e': 'Elderberry',
        'f': 'Fig',
        'g': 'Grape',
        'h': 'Honeydew',
        'i': 'Indian Prune',
        'j': 'Jackfruit'
    }
    counter, ax = task_func(fruit_dict)
    assert counter == Counter(FRUITS)
    assert len(ax.patches) == len(FRUITS)

def test_task_func_with_invalid_fruits():
    fruit_dict = {
        'a': 'Apple',
        'b': 'Banana',
        'c': 'Cherry',
        'd': 'Date',
        'e': 'Elderberry',
        'f': 'Fig',
        'g': 'Grape',
        'h': 'Honeydew',
        'i': 'Indian Prune',
        'j': 'Jackfruit',
        'k': 'Kumquat',  # Invalid fruit
        'l': 'Lemon'     # Invalid fruit
    }
    counter, ax = task_func(fruit_dict)
    assert counter == Counter(FRUITS)
    assert len(ax.patches) == len(FRUITS)

def test_task_func_with_no_valid_fruits():
    fruit_dict = {
        'a': 'Apricot',  # Invalid fruit
        'b': 'Blueberry',  # Invalid fruit
        'c': 'Cantaloupe',  # Invalid fruit
    }
    counter, ax = task_func(fruit_dict)
    assert counter == Counter()
    assert len(ax.patches) == 0

def test_task_func_with_empty_dict():
    fruit_dict = {}
    counter, ax = task_func(fruit_dict)
    assert counter == Counter()
    assert len(ax.patches) == 0

def test_task_func_with_mixed_types():
    fruit_dict = {
        'a': 'Apple',
        'b': 123,  # Invalid type
        'c': 'Cherry',
        'd': None,  # Invalid type
        'e': 'Elderberry',
        'f': 'Fig',
        'g': 'Grape',
        'h': 'Honeydew',
        'i': 'Indian Prune',
        'j': 'Jackfruit'
    }
    counter, ax = task_func(fruit_dict)
    assert counter == Counter(FRUITS)
    assert len(ax.patches) == len(FRUITS)