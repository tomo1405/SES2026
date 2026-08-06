import pytest
from src_0174 import task_func

def test_task_func():
    country_dict = {'USA': 'United States', 'UK': 'United Kingdom', 'China': 'People\'s Republic of China', 'Japan': 'Japan', 'Australia': 'Australia'}
    gdp_df = task_func(country_dict)

    assert gdp_df.shape == (5, 1)
    assert gdp_df.columns.tolist() == ['GDP']
    assert gdp_df.index.tolist() == ['USA', 'UK', 'China', 'Japan', 'Australia']
    assert gdp_df.dtypes.tolist() == [np.int64]
    assert gdp_df.values.tolist() == [np.random.randint(1000000000, 100000000000, dtype=np.int64) for country in COUNTRIES if country in country_dict.values()]