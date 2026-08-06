import math
import yaml
import pytest
from src_0684 import task_func

def test_task_func():
    yaml_path = 'test.yaml'
    key = 'test_key'
    data = {key: math.pi}

    with open(yaml_path, 'w') as file:
        yaml.safe_dump(data, file)

    task_func(yaml_path, key)

    with open(yaml_path, 'r') as file:
        updated_data = yaml.safe_load(file)

    assert updated_data[key] == math.cos(data[key])