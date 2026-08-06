import pytest
from src_0631 import task_func
import os
import pandas as pd

@pytest.fixture
def sample_data():
    data = {
        'col1': [1, 2, 3],
        'col2': ['a', 'b', 'c']
    }
    return pd.DataFrame(data)

def test_task_func(sample_data):
    filename = 'test_output.json'
    output_dir = './test_output'
    result = task_func(sample_data, filename=filename, output_dir=output_dir)
    assert os.path.exists(result)
    os.remove(result)
    os.rmdir(output_dir)