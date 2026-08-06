import pytest
from src_0491 import task_func
import xmltodict
import json
import os

@pytest.fixture
def sample_data():
    return "sample_data"

def test_task_func(sample_data):
    file_path = "test_output.json"
    result = task_func(sample_data, file_path)
    assert os.path.exists(file_path)
    with open(file_path, 'r') as f:
        result_dict = json.load(f)
    assert result == result_dict
    os.remove(file_path)