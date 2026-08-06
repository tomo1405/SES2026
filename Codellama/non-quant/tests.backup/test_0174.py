import pytest
from src_0174 import task_func

def test_task_func():
    country_dict = {'USA': 'United States', 'UK': 'United Kingdom', 'China': 'People\'s Republic of China', 'Japan': 'Japan', 'Australia': 'Australia'}
    gdp_df = task_func(country_dict)

    assert gdp_df.shape == (5, 1)
    assert gdp_df.columns.to_list() == ['GDP']
    assert gdp_df.index.to_list() == ['USA', 'UK', 'China', 'Japan', 'Australia']
    assert gdp_df['GDP'].dtype == np.int64
    assert gdp_df['GDP'].min() >= 1000000000
    assert gdp_df['GDP'].max() <= 100000000000