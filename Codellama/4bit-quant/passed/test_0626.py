import pytest
from src_0626 import task_func

def test_task_func():
    cities_list = ['New York', 'Los Angeles', 'Chicago', 'Houston']
    population_df = task_func(cities_list)

    assert population_df.columns.tolist() == ['City', 'Population']
    assert len(population_df) == len(cities_list)
    assert all(population_df['City'] == cities_list)
    assert all(population_df['Population'] >= 1000000)
    assert all(population_df['Population'] <= 20000000)
    assert all(population_df['Population'] % 1000 == 0)