import pytest
from src_0865 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_data():
    return [(1, 2), (2, 3), (1, 4), (2, 5)]

def test_task_func(sample_data):
    result = task_func(sample_data)
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert not result.empty, "The DataFrame should not be empty"
    assert set(result.columns) == {'Total Count', 'Average Count'}, "Columns should be 'Total Count' and 'Average Count'"