import matplotlib.pyplot as plt
import pytest
from src_0388 import task_func


def test_task_func_with_valid_input():
    city_dict = {'city1': 'New York', 'city2': 'London', 'city3': 'Tokyo'}
    expected_cities = set(['New York', 'London', 'Tokyo'])
    city_population, ax = task_func(city_dict)

    assert isinstance(city_population, dict)
    assert set(city_population.keys()) == expected_cities
    for city, population in city_population.items():
        assert 1 <= population <= 1000000

    assert isinstance(ax, plt.Axes)

def test_task_func_with_invalid_city():
    city_dict = {'city1': 'InvalidCity', 'city2': 'New York'}
    city_population, ax = task_func(city_dict)

    assert isinstance(city_population, dict)
    assert city_population['InvalidCity'] == -1
    assert 1 <= city_population['New York'] <= 1000000

    assert isinstance(ax, plt.Axes)

def test_task_func_with_max_range_zero():
    city_dict = {'city1': 'New York'}
    with pytest.raises(ValueError):
        task_func(city_dict, max_range=0)

def test_task_func_with_negative_max_range():
    city_dict = {'city1': 'New York'}
    with pytest.raises(ValueError):
        task_func(city_dict, max_range=-1000)

def test_task_func_with_non_string_city():
    city_dict = {'city1': 12345, 'city2': 'New York'}
    city_population, ax = task_func(city_dict)

    assert isinstance(city_population, dict)
    assert len(city_population) == 1
    assert 'New York' in city_population
    assert 1 <= city_population['New York'] <= 1000000

    assert isinstance(ax, plt.Axes)

def test_task_func_with_empty_dict():
    city_dict = {}
    city_population, ax = task_func(city_dict)

    assert isinstance(city_population, dict)
    assert len(city_population) == 0

    assert isinstance(ax, plt.Axes)

def test_task_func_with_all_invalid_cities():
    city_dict = {'city1': 'InvalidCity1', 'city2': 'InvalidCity2'}
    city_population, ax = task_func(city_dict)

    assert isinstance(city_population, dict)
    assert city_population['InvalidCity1'] == -1
    assert city_population['InvalidCity2'] == -1

    assert isinstance(ax, plt.Axes)