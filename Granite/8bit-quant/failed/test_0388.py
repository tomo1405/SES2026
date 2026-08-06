import pytest
from src_0388 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    city_dict = {'New York': 'NY', 'London': 'London', 'Beijing': 'BJ', 'Tokyo': 'TK', 'Sydney': 'SY', 'Paris': 'PR', 'Berlin': 'Berlin', 'Moscow': 'Moscow', 'Madrid': 'Madrid', 'Rome': 'Rome'}
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

def test_task_func_invalid_max_range():
    city_dict = {'New York': 'NY', 'London': 'London', 'Beijing': 'BJ', 'Tokyo': 'TK', 'Sydney': 'SY', 'Paris': 'PR', 'Berlin': 'Berlin', 'Moscow': 'Moscow', 'Madrid': 'Madrid', 'Rome': 'Rome'}
    max_range = 0
    seed = 0
    with pytest.raises(ValueError) as excinfo:
        task_func(city_dict, max_range, seed)
    assert str(excinfo.value) == "max_range must be a positive integer"