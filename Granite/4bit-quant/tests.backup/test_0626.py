import math
from random import randint
import pandas as pd
from src_0626 import task_func

def test_task_func():
    cities_list = ['New York', 'Los Angeles', 'Chicago', 'Houston']
    population_df = task_func(cities_list)
    assert isinstance(population_df, pd.DataFrame)
    assert list(population_df.columns) == ['City', 'Population']
    assert len(population_df) == len(cities_list)
    for city, population in population_df.values:
        assert isinstance(city, str)
        assert isinstance(population, int)
        assert population >= 1000000 and population <= 20000000