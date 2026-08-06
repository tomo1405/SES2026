import pytest
from src_0682 import task_func
import pandas as pd
import json

@pytest.fixture
def sample_data():
    data = {
        "key1": "value1",
        "key2": "value2"
    }
    return data

def test_task_func(sample_data):
    file_path = "test_file.json"
    result = task_func(file_path, key="key1")
    assert result is not None
    assert len(result) == 1