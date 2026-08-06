python
import pandas as pd
import pytest
from src_0305 import task_func

def test_task_func():
    # Test case 1: Empty dataframe
    df = pd.DataFrame()
    assert task_func(df) == (0,0)
    
    # Test case 2: Valid dataframe
    df = pd.DataFrame({'Date': ['2021-01-01', '2021-01-02', '2021-01-03'], 'Value': [1,2,3]})
    explained_variance_ratio, ax = task_func(df)
    assert len(explained_variance_ratio) == 2
    assert ax.get_title() == 'Explained Variance Ratio of Principal Components'
    assert ax.get_xlabel() == 'Principal Component'
    assert ax.get_ylabel() == 'Explained Variance Ratio'