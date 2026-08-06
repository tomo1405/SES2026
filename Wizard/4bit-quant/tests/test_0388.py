python
import numpy as np
import matplotlib.pyplot as plt
from src_0388 import task_func

def test_task_func():
    # Test case 1: Valid input
    city_dict = {'New York': 8398748, 'London': 8988567, 'Beijing': 21516000, 'Tokyo': 13923700, 'Sydney': 5330000, 'Paris': 2249975, 'Berlin': 3671666, 'Moscow': 12544000, 'Madrid': 6452624, 'Rome': 2872266}
    max_range = 1000000
    seed = 0
    expected_city_population = {'New York': 8398748, 'London': 8988567, 'Beijing': 21516000, 'Tokyo': 13923700, 'Sydney': 5330000, 'Paris': 2249975, 'Berlin': 3671666, 'Moscow': 12544000, 'Madrid': 6452624, 'Rome': 2872266}
    expected_ax = plt.figure().gca()

    city_population, ax = task_func(city_dict, max_range, seed)

    assert city_population == expected_city_population
    assert ax == expected_ax

    # Test case 2: Invalid input (max_range < 1)
    city_dict = {'New York': 8398748, 'London': 8988567, 'Beijing': 21516000, 'Tokyo': 13923700, 'Sydney': 5330000, 'Paris': 2249975, 'Berlin': 3671666, 'Moscow': 12544000, 'Madrid': 6452624, 'Rome': 2872266}
    max_range = 0
    seed = 0

    try:
        city_population, ax = task_func(city_dict, max_range, seed)
        assert False
    except ValueError:
        assert True

    # Test case 3: Invalid input (city_dict contains non-string key)
    city_dict = {'New York': 8398748, 'London': 8988567, 'Beijing': 21516000, 'Tokyo': 13923700, 'Sydney': 5330000, 'Paris': 2249975, 'Berlin': 3671666, 'Moscow': 12544000, 'Madrid': 6452624, 123: 'Rome'}
    max_range = 1000000
    seed = 0

    try:
        city_population, ax = task_func(city_dict, max_range, seed)
        assert False
    except ValueError:
        assert True