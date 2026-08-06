python
import pandas as pd
import random
import pytest

from src_0812 import task_func

def test_task_func():
    # Test case 1: sample_size is None and random_seed is None
    dictionary = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
    item = 5
    expected_result = [(0, 'B'), (1, 'B'), (2, 'B')]
    result = task_func(dictionary, item, sample_size=None, random_seed=None)
    assert result[0] == expected_result
    assert isinstance(result[1], pd.DataFrame)

    # Test case 2: sample_size is None and random_seed is not None
    random_seed = 123
    expected_result = [(1, 'B'), (2, 'B'), (0, 'B')]
    result = task_func(dictionary, item, sample_size=None, random_seed=random_seed)
    assert result[0] == expected_result
    assert isinstance(result[1], pd.DataFrame)

    # Test case 3: sample_size is not None and random_seed is None
    sample_size = 2
    expected_result = [(1, 'B'), (2, 'B')]
    result = task_func(dictionary, item, sample_size=sample_size, random_seed=None)
    assert result[0] == expected_result
    assert isinstance(result[1], pd.DataFrame)

    # Test case 4: sample_size is not None and random_seed is not None
    sample_size = 2
    random_seed = 123
    expected_result = [(2, 'B'), (1, 'B')]
    result = task_func(dictionary, item, sample_size=sample_size, random_seed=random_seed)
    assert result[0] == expected_result
    assert isinstance(result[1], pd.DataFrame)

    # Test case 5: item not found in dictionary
    dictionary = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
    item = 10
    expected_result = [], pd.DataFrame(dictionary)
    result = task_func(dictionary, item, sample_size=None, random_seed=None)
    assert result == expected_result

    # Test case 6: sample_size is greater than the number of occurrences of item in dictionary
    dictionary = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
    item = 5
    sample_size = 5
    expected_result = [(0, 'B'), (1, 'B'), (2, 'B')]
    result = task_func(dictionary, item, sample_size=sample_size, random_seed=None)
    assert result[0] == expected_result
    assert isinstance(result[1], pd.DataFrame)