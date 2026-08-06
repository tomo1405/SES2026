import pytest
from src_0388 import task_func

def test_task_func_valid_input():
    city_dict = {'New York': 'USA', 'London': 'UK', 'Beijing': 'China', 'Tokyo': 'Japan', 'Sydney': 'Australia', 'Paris': 'France', 'Berlin': 'Germany', 'Moscow': 'Russia', 'Madrid': 'Spain', 'Rome': 'Italy'}
    city_population, ax = task_func(city_dict)
    assert city_population == {'New York': 123456, 'London': 234567, 'Beijing': 345678, 'Tokyo': 456789, 'Sydney': 567890, 'Paris': 678901, 'Berlin': 789012, 'Moscow': 890123, 'Madrid': 901234, 'Rome': 1234567}
    assert ax.get_xlabel() == 'City'
    assert ax.get_ylabel() == 'Population'
    assert ax.get_title() == 'City Populations'

def test_task_func_invalid_input():
    city_dict = {'New York': 'USA', 'London': 'UK', 'Beijing': 'China', 'Tokyo': 'Japan', 'Sydney': 'Australia', 'Paris': 'France', 'Berlin': 'Germany', 'Moscow': 'Russia', 'Madrid': 'Spain', 'Rome': 'Italy'}
    with pytest.raises(ValueError):
        task_func(city_dict, max_range=0)