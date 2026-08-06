import pytest
from src_0892 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_data():
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'target': [2, 3, 4, 5, 6]
    }
    df = pd.DataFrame(data)
    temp_file = 'temp.csv'
    df.to_csv(temp_file, index=False)
    yield temp_file
    import os
    os.remove(temp_file)

def test_task_func(sample_data):
    model, predictions = task_func(sample_data, 'target', test_size=0.2, random_state=42)
    
    assert isinstance(model, LinearRegression)
    assert isinstance(predictions, np.ndarray)
    assert len(predictions) == 1  # Since test_size is 0.2, 1 out of 5 rows is used for testing

def test_task_func_with_different_random_state(sample_data):
    model1, predictions1 = task_func(sample_data, 'target', test_size=0.2, random_state=0)
    model2, predictions2 = task_func(sample_data, 'target', test_size=0.2, random_state=1)
    
    assert not np.array_equal(predictions1, predictions2), "Predictions should differ with different random states"