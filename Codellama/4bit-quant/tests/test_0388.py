import pytest
from src_0388 import task_func

def test_task_func():
    # Test 1: max_range is a positive integer
    city_dict = {'New York': 'NY', 'London': 'UK', 'Beijing': 'CN', 'Tokyo': 'JP', 'Sydney': 'AU', 'Paris': 'FR', 'Berlin': 'DE', 'Moscow': 'RU', 'Madrid': 'ES', 'Rome': 'IT'}
    max_range = 1000000
    seed = 0
    city_population, ax = task_func(city_dict, max_range, seed)
    assert city_population == {'New York': 1000000, 'London': 1000000, 'Beijing': 1000000, 'Tokyo': 1000000, 'Sydney': 1000000, 'Paris': 1000000, 'Berlin': 1000000, 'Moscow': 1000000, 'Madrid': 1000000, 'Rome': 1000000}
    assert ax.get_xlabel() == 'City'
    assert ax.get_ylabel() == 'Population'
    assert ax.get_title() == 'City Populations'

    # Test 2: max_range is not a positive integer
    max_range = 0
    with pytest.raises(ValueError):
        task_func(city_dict, max_range, seed)

    # Test 3: city_dict contains invalid keys
    city_dict = {'New York': 'NY', 'London': 'UK', 'Beijing': 'CN', 'Tokyo': 'JP', 'Sydney': 'AU', 'Paris': 'FR', 'Berlin': 'DE', 'Moscow': 'RU', 'Madrid': 'ES', 'Rome': 'IT', 'Invalid': 'IN'}
    with pytest.raises(ValueError):
        task_func(city_dict, max_range, seed)

    # Test 4: city_dict contains invalid values
    city_dict = {'New York': 'NY', 'London': 'UK', 'Beijing': 'CN', 'Tokyo': 'JP', 'Sydney': 'AU', 'Paris': 'FR', 'Berlin': 'DE', 'Moscow': 'RU', 'Madrid': 'ES', 'Rome': 'IT', 'Invalid': 'IN'}
    with pytest.raises(ValueError):
        task_func(city_dict, max_range, seed)