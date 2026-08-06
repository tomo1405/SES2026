import pytest
from src_0076 import task_func
import pandas as pd
import numpy as np
import itertools
from datetime import datetime, timedelta
import seaborn as sns

@pytest.fixture
def sample_data():
    df = pd.DataFrame({
        'Column1': [1, 2, 3],
        'Column2': ['A', 'B', 'C']
    })
    return df

def test_task_func(sample_data):
    df = sample_data
    result, plot = task_func(df)
    assert isinstance(result, pd.DataFrame)
    assert isinstance(plot, sns.axisgrid.BoxPlot)