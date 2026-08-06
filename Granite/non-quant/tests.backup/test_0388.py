import pytest
from src_0388 import task_func
import numpy as np
import matplotlib.pyplot as plt

CITIES = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney', 'Paris', 'Berlin', 'Moscow', 'Madrid', 'Rome']

def test_task_func_with_valid_input():
    city_dict = {1: 'New York', 2: 'London', 3: 'Beijing', 4: 'Tokyo', 5: 'Sydney', 6: 'Paris', 7: 'Berlin', 8: 'Moscow', 9: 'Madrid', 10: 'Rome'}
    max_range = 1000000
    seed = 0
    city_population, ax = task_func(city_dict, max_range, seed)
    assert isinstance(city_population, dict)
    assert isinstance(ax, plt.Axes)
    assert len(city_population) == len(city_dict)
    for city, population in city_population.items():
        assert city in city_dict.values()
        if city in CITIES:
            assert 1 <= population <= max_range
        else:
            assert population == -1
    assert ax.get_xlabel() == 'City'
    assert ax.get_ylabel() == 'Population'
    assert ax.get_title() == 'City Populations'

def test_task_func_with_invalid_max_range():
    city_dict = {1: 'New York', 2: 'London', 3: 'Beijing', 4: 'Tokyo', 5: 'Sydney', 6: 'Paris', 7: 'Berlin', 8: 'Moscow', 9: 'Madrid', 10: 'Rome'}
    max_range = 0
    seed = 0
    with pytest.raises(ValueError) as excinfo:
        task_func(city_dict, max_range, seed)
    assert str(excinfo.value) == "max_range must be a positive integer"