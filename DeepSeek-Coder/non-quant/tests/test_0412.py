import pytest
from src_0412 import task_func
import pandas as pd
import json

@pytest.fixture
def sample_data():
    return {
        "a": 1,
        "b": 2,
        "c": 3
    }

def test_task_func(sample_data):
    output_path = "test_output.json"
    result = task_func(sample_data, output_path=output_path)
    assert result == output_path
    with open(output_path, "r") as file:
        data = json.load(file)
    assert data == {"a": 1, "b": 2}