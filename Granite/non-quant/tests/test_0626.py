import pytest
from src_0626 import task_func
import math
from random import randint
import pandas as pd

@pytest.fixture
def cities_list():
    return ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']

def test_task_func(cities_list):
    population_df = task_func(cities_list)
    assert isinstance(population_df, pd.DataFrame)
    assert population_df.shape == (len(cities_list), 2)
    assert population_df.columns.tolist() == ['City', 'Population']
    for city, population in population_df.values:
        assert isinstance(city, str)
        assert isinstance(population, int)
        assert population >= 1000000 and population <= 20000000

def test_task_func_empty_list(cities_list):
    empty_list = []
    with pytest.raises(ValueError):
        task_func(empty_list)

def test_task_func_non_list(cities_list):
    non_list = 123
    with pytest.raises(TypeError):
        task_func(non_list)