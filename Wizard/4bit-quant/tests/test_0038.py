python
import pandas as pd
import pytest
from src_0038 import task_func

@pytest.fixture
def sample_data():
    data = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9], 'target': [0, 1, 0]}
    df = pd.DataFrame(data)
    return df

def test_task_func(sample_data):
    model, ax = task_func(sample_data, 'target')
    assert isinstance(model, RandomForestClassifier)
    assert isinstance(ax, sns.axisgrid.FacetGrid)