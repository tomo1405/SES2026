import pytest
from src_0890 import task_func
import pandas as pd
import numpy as np
import os

@pytest.fixture
def sample_data():
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': [100, 200, 300, 400, 500]
    }
    df = pd.DataFrame(data)
    return df

def test_task_func(sample_data):
    result = task_func("dummy_dir", "dummy_file.csv")
    assert result.equals(sample_data)