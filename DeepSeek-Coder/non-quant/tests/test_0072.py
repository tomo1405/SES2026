import pytest
from src_0072 import task_func
import pandas as pd
import seaborn as sns
import numpy as np
import ast

@pytest.fixture
def sample_data():
    data = {
        'list': [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    }
    df = pd.DataFrame(data)
    return df

def test_task_func(sample_data):
    df, plot = task_func('dummy_file.csv')
    assert isinstance(df, pd.DataFrame), "The result should be a DataFrame"
    assert 'sum' in df.columns, "The DataFrame should have a 'sum' column"
    assert 'mean' in df.columns, "The DataFrame should have a 'mean' column"
    assert 'std' in df.columns, "The DataFrame should have a 'std' column"
    assert isinstance(plot, sns.axisgrid.FacetGrid), "The plot should be a seaborn plot"