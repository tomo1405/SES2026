import pytest
from src_0812 import task_func

def test_task_func_positions():
    dictionary = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
    item = 5
    sample_size = 2
    random_seed = 1234

    positions, dataframe = task_func(dictionary, item, sample_size, random_seed)

    assert positions == [(1, 'b'), (2, 'b')]
    assert dataframe.equals(pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}))

def test_task_func_positions_no_sample_size():
    dictionary = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
    item = 5
    sample_size = None
    random_seed = 1234

    positions, dataframe = task_func(dictionary, item, sample_size, random_seed)

    assert positions == [(1, 'b'), (2, 'b')]
    assert dataframe.equals(pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}))

def test_task_func_positions_no_random_seed():
    dictionary = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
    item = 5
    sample_size = 2
    random_seed = None

    positions, dataframe = task_func(dictionary, item, sample_size, random_seed)

    assert positions == [(1, 'b'), (2, 'b')]
    assert dataframe.equals(pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}))

def test_task_func_positions_no_sample_size_no_random_seed():
    dictionary = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
    item = 5
    sample_size = None
    random_seed = None

    positions, dataframe = task_func(dictionary, item, sample_size, random_seed)

    assert positions == [(1, 'b'), (2, 'b')]
    assert dataframe.equals(pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}))