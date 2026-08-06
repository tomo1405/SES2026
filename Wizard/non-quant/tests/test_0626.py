python
import math
import random
import pandas as pd
import pytest

from src_0626 import task_func

def test_task_func():
    cities_list = ['New York', 'Los Angeles', 'Chicago', 'Houston']
    population_data = []

    for city in cities_list:
        population = math.ceil(random.randint(1000000, 20000000) / 1000.0) * 1000
        population_data.append([city, population])

    population_df = pd.DataFrame(population_data, columns=['City', 'Population'])

    assert task_func(cities_list) == population_df