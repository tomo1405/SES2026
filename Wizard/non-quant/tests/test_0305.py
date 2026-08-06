python
import pandas as pd
import pytest
from src_0305 import task_func

def test_task_func():
    # Test case 1: Test with empty dataframe
    df = pd.DataFrame()
    explained_variance_ratio, ax = task_func(df)
    assert explained_variance_ratio == 0
    assert ax == None
    
    # Test case 2: Test with valid dataframe
    df = pd.DataFrame({'Date': ['2021-01-01', '2021-01-02', '2021-01-03'], 'Value': [1, 2, 3]})
    explained_variance_ratio, ax = task_func(df)
    assert len(explained_variance_ratio) == 2
    assert ax != None