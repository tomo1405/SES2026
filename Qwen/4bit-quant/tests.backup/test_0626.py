import pytest
from src_0626 import task_func
import pandas as pd

def test_task_func_output_type():
    cities_list = ['New York', 'Los Angeles', 'Chicago']
    result = task_func(cities_list)
    assert isinstance(result, pd.DataFrame)

def test_task_func_columns():
    cities_list = ['New York', 'Los Angeles', 'Chicago']
    result = task_func(cities_list)
    assert list(result.columns) == ['City', 'Population']

def test_task_func_city_values():
    cities_list = ['New York', 'Los Angeles', 'Chicago']
    result = task_func(cities_list)
    assert all(city in result['City'].values for city in cities_list)

def test_task_func_population_range():
    cities_list = ['New York', 'Los Angeles', 'Chicago']
    result = task_func(cities_list)
    assert all(1000000 <= pop <= 20000000 for pop in result['Population'])

def test_task_func_population_multiples_of_1000():
    cities_list = ['New York', 'Los Angeles', 'Chicago']
    result = task_func(cities_list)
    assert all(pop % 1000 == 0 for pop in result['Population'])