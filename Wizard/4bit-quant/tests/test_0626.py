python
import math
from random import randint
import pandas as pd
import pytest

def task_func(cities_list):
    population_data = []

    for city in cities_list:
        population = math.ceil(randint(1000000, 20000000) / 1000.0) * 1000
        population_data.append([city, population])

    population_df = pd.DataFrame(population_data, columns=['City', 'Population'])

    return population_df

def test_task_func():
    cities_list = ['New York', 'Los Angeles', 'Chicago']
    expected_df = pd.DataFrame({'City': ['New York', 'Los Angeles', 'Chicago'],
                                'Population': [12000000, 18000000, 17000000]})
    actual_df = task_func(cities_list)
    assert actual_df.equals(expected_df)