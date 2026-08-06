import pandas as pd
from src_0626 import task_func


def test_task_func():
    cities_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
    population_df = task_func(cities_list)

    assert isinstance(population_df, pd.DataFrame)
    assert population_df.shape[0] == len(cities_list)
    assert population_df.shape[1] == 2
    assert all(population_df['City'] == cities_list)
    assert all(population_df['Population'] >= 1000000)
    assert all(population_df['Population'] <= 20000000)
    assert all(population_df['Population'] % 1000 == 0)