import pytest
from src_0174 import task_func

def test_task_func():
    country_dict = {'USA': 'United States', 'UK': 'United Kingdom', 'China': 'People\'s Republic of China', 'Japan': 'Japan', 'Australia': 'Australia'}
    gdp_df = task_func(country_dict)
    assert gdp_df.shape == (4, 1)
    assert gdp_df.columns.to_list() == ['GDP']
    assert gdp_df.index.to_list() == ['USA', 'UK', 'China', 'Japan']
    assert gdp_df.dtypes.to_list() == [np.int64]