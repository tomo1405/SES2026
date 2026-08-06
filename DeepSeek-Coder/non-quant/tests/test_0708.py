import pytest
from src_0708 import task_func
import numpy as np
import pandas as pd

@pytest.fixture
def sample_data():
    data = {
        'IntCol': [10, 100, 1000]
    }
    df = pd.DataFrame(data)
    return df

def test_task_func(sample_data):
    result = task_func(sample_data)
    assert 'IntCol' in result.columns
    assert result['IntCol'].iloc[0] == np.log10(10)
    assert result['IntCol'].iloc[1] == np.log10(100)
    assert result['IntCol'].iloc[2] == np.log10(1000)
    with open('IntCol.json', 'r') as json_file:
        content = json.load(json_file)
        assert content == [np.log10(10), np.log10(100), np.log10(1000)]