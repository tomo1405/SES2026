python
import pytest
from src_0174 import task_func

def test_task_func():
    country_dict = {'USA': 'USA', 'UK': 'UK', 'China': 'China', 'Japan': 'Japan', 'Australia': 'Australia'}
    gdp_df = task_func(country_dict)
    assert isinstance(gdp_df, pd.DataFrame)
    assert len(gdp_df) == 5
    assert 'GDP' in gdp_df.columns
    assert all(isinstance(gdp, int) for gdp in gdp_df['GDP'])