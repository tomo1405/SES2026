import pytest
import numpy as np
import matplotlib.pyplot as plt
from src_0388 import task_func

CITIES = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney', 'Paris', 'Berlin', 'Moscow', 'Madrid', 'Rome']

def test_task_func():
    city_dict = {'New York': 'NY', 'London': 'LDN', 'Beijing': 'BJS', 'Tokyo': 'NRT'}
    max_range = 1000000
    seed = 0
    city_population, ax = task_func(city_dict, max_range, seed)
    assert isinstance(city_population, dict)
    assert all(isinstance(city, str) for city in city_population.keys())
    assert all(isinstance(population, int) for population in city_population.values())
    assert all(population >= 1 and population <= max_range for population in city_population.values())
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'City'
    assert ax.get_ylabel() == 'Population'
    assert ax.get_title() == 'City Populations'

def test_task_func_invalid_max_range():
    city_dict = {'New York': 'NY', 'London': 'LDN', 'Beijing': 'BJS', 'Tokyo': 'NRT'}
    max_range = 0
    seed = 0
    with pytest.raises(ValueError):
        task_func(city_dict, max_range, seed)