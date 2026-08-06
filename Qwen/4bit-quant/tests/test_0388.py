import pytest
from src_0388 import task_func
import numpy as np

def test_task_func_with_valid_input():
    city_dict = {'city1': 'New York', 'city2': 'London', 'city3': 'Paris'}
    max_range = 1000000
    seed = 0

    result, ax = task_func(city_dict, max_range, seed)

    assert isinstance(result, dict)
    assert len(result) == 3
    assert all(isinstance(value, int) and value >= 0 for value in result.values())

    # Check that the cities are correctly mapped to their populations
    assert 'New York' in result
    assert 'London' in result
    assert 'Paris' in result

    # Check that the plot is created with the correct number of bars
    assert len(ax.patches) == 3

def test_task_func_with_invalid_max_range():
    city_dict = {'city1': 'New York', 'city2': 'London', 'city3': 'Paris'}
    max_range = -1
    seed = 0

    with pytest.raises(ValueError, match="max_range must be a positive integer"):
        task_func(city_dict, max_range, seed)

def test_task_func_with_non_string_city():
    city_dict = {'city1': 'New York', 'city2': 12345, 'city3': 'Paris'}
    max_range = 1000000
    seed = 0

    result, ax = task_func(city_dict, max_range, seed)

    assert isinstance(result, dict)
    assert len(result) == 2
    assert all(isinstance(value, int) and value >= 0 for value in result.values())

    # Check that the cities are correctly mapped to their populations
    assert 'New York' in result
    assert 'Paris' in result

    # Check that the plot is created with the correct number of bars
    assert len(ax.patches) == 2

def test_task_func_with_city_not_in_CITIES():
    city_dict = {'city1': 'New York', 'city2': 'Oslo', 'city3': 'Paris'}
    max_range = 1000000
    seed = 0

    result, ax = task_func(city_dict, max_range, seed)

    assert isinstance(result, dict)
    assert len(result) == 2
    assert all(isinstance(value, int) and value >= 0 for value in result.values())

    # Check that the cities are correctly mapped to their populations
    assert 'New York' in result
    assert 'Paris' in result
    assert result['Oslo'] == -1

    # Check that the plot is created with the correct number of bars
    assert len(ax.patches) == 2