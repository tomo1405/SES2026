import pytest
from src_0388 import task_func
import numpy as np
import matplotlib.pyplot as plt

# Mocking the random number generation to ensure predictable results
class TestTaskFunc:
    def test_task_func_with_valid_input(self):
        city_dict = {'city1': 'New York', 'city2': 'London', 'city3': 'Paris'}
        expected_cities = ['New York', 'London', 'Paris']
        expected_values = [500000, 900000, 200000]  # Example values, will be replaced by mock
        np.random.seed(0)  # Ensuring reproducibility
        mock_random = np.random.RandomState(0)
        with pytest.MonkeyPatch.context() as mp:
            mp.setattr(np.random, 'randint', lambda low, high, size=None: mock_random.randint(low, high, size))
            result, ax = task_func(city_dict, max_range=1000000, seed=0)
        
        assert list(result.keys()) == expected_cities
        assert all(result[city] in expected_values for city in expected_cities)
        assert isinstance(ax, plt.Axes)

    def test_task_func_with_invalid_max_range(self):
        city_dict = {'city1': 'New York', 'city2': 'London', 'city3': 'Paris'}
        with pytest.raises(ValueError, match="max_range must be a positive integer"):
            task_func(city_dict, max_range=-1, seed=0)

    def test_task_func_with_non_string_city(self):
        city_dict = {'city1': 'New York', 'city2': 12345, 'city3': 'Paris'}
        expected_cities = ['New York', 'Paris']
        expected_values = [500000, 200000]  # Example values, will be replaced by mock
        np.random.seed(0)  # Ensuring reproducibility
        mock_random = np.random.RandomState(0)
        with pytest.MonkeyPatch.context() as mp:
            mp.setattr(np.random, 'randint', lambda low, high, size=None: mock_random.randint(low, high, size))
            result, ax = task_func(city_dict, max_range=1000000, seed=0)
        
        assert list(result.keys()) == expected_cities
        assert all(result[city] in expected_values for city in expected_cities)
        assert isinstance(ax, plt.Axes)

    def test_task_func_with_empty_city_dict(self):
        city_dict = {}
        result, ax = task_func(city_dict, max_range=1000000, seed=0)
        assert result == {}
        assert isinstance(ax, plt.Axes)

    def test_task_func_with_all_cities_not_in_list(self):
        city_dict = {'city1': 'Oslo', 'city2': 'Vienna', 'city3': 'Stockholm'}
        result, ax = task_func(city_dict, max_range=1000000, seed=0)
        assert all(value == -1 for value in result.values())
        assert isinstance(ax, plt.Axes)