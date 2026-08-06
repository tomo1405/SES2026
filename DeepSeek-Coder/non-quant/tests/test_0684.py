import pytest
from src_0684 import task_func
import yaml
import math

@pytest.fixture
def setup():
    return "test.yaml"

def test_task_func(setup):
    yaml_path = setup
    key = "test_key"
    data = {key: 0}
    with open(yaml_path, 'w') as file:
        yaml.safe_dump(data, file)

    result = task_func(yaml_path, key)

    with open(yaml_path, 'r') as file:
        loaded_data = yaml.safe_load(file)
    
    assert key in loaded_data
    assert loaded_data[key] == math.cos(data[key])