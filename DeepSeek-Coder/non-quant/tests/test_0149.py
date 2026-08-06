import pytest
from src_0149 import task_func
import pandas as pd
from sklearn.preprocessing import LabelEncoder

@pytest.fixture
def sample_data():
    data = {
        'category': ['A', 'B', 'A', 'B', 'A'],
        'value': [1, 2, 3, 4, 5]
    }
    return pd.DataFrame(data)

def test_task_func(sample_data):
    result = task_func(sample_data, 'category')
    assert result['category'].tolist() == [0, 1, 0, 1, 0]