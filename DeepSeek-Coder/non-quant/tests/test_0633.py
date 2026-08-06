import pytest
from src_0633 import task_func
import pandas as pd
import os
import json
import time

@pytest.fixture
def sample_dataframe():
    data = {
        'col1': [1, 2, 3],
        'col2': ['a', 'b', 'c']
    }
    return pd.DataFrame(data)

def test_task_func(sample_dataframe):
    filename = "test_output.json"
    result = task_func(sample_dataframe, filename=filename)
    assert os.path.exists(result)
    os.remove(result)  # Clean up