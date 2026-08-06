import pytest
from src_0388 import task_func

def test_task_func_valid_input():
    city_dict = {'New York': 'USA', 'London': 'UK', 'Beijing': 'China', 'Tokyo': 'Japan', 'Sydney': 'Australia', 'Paris': 'France', 'Berlin': 'Germany', 'Moscow': 'Russia', 'Madrid': 'Spain', 'Rome': 'Italy'}
    city_population, ax = task_func(city_dict)
    assert isinstance(city_population, dict)
    assert all(isinstance(city, str) for city in city_population.keys())
    assert all(isinstance(population, int) for population in city_population.values())
    assert ax.get_xlabel() == 'City'
    assert ax.get_ylabel() == 'Population'
    assert ax.get_title() == 'City Populations'

def test_task_func_invalid_input():
    city_dict = {'New York': 'USA', 'London': 'UK', 'Beijing': 'China', 'Tokyo': 'Japan', 'Sydney': 'Australia', 'Paris': 'France', 'Berlin': 'Germany', 'Moscow': 'Russia', 'Madrid': 'Spain', 'Rome': 'Italy'}
    with pytest.raises(ValueError):
        task_func(city_dict, max_range=0)

def test_task_func_invalid_city():
    city_dict = {'New York': 'USA', 'London': 'UK', 'Beijing': 'China', 'Tokyo': 'Japan', 'Sydney': 'Australia', 'Paris': 'France', 'Berlin': 'Germany', 'Moscow': 'Russia', 'Madrid': 'Spain', 'Rome': 'Italy'}
    with pytest.raises(ValueError):
        task_func(city_dict, city_dict={'New York': 'USA', 'London': 'UK', 'Beijing': 'China', 'Tokyo': 'Japan', 'Sydney': 'Australia', 'Paris': 'France', 'Berlin': 'Germany', 'Moscow': 'Russia', 'Madrid': 'Spain', 'Rome': 'Italy', 'Invalid City': 'Invalid Country'})