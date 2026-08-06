python
import pytest
from src_0086 import task_func

def test_task_func():
    start_date = '2021-01-01'
    end_date = '2021-01-05'
    random_seed = 42
    
    df, ax = task_func(start_date, end_date, random_seed)
    
    assert df.shape == (5, 4)
    assert ax.get_title() == "Generated Weather Data"