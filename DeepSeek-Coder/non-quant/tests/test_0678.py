import pytest
from src_0678 import task_func
import numpy as np
import pandas as pd
from scipy.stats import linregress

@pytest.fixture
def sample_data():
    data = {
        'var1': [1, 2, 3, 4, 5],
        'var2': [2, 3, 4, 5, 6]
    }
    df = pd.DataFrame(data)
    return df

def test_task_func(sample_data):
    result = task_func(sample_data)
    assert 'predicted' in result.columns
    assert all(result['predicted'] == [3, 5, 7, 9, 11])