import pytest
from src_0684 import task_func

def test_task_func():
    yaml_path = 'test_data.yaml'
    key = 'test_key'
    data = {'test_key': 1.0}

    with open(yaml_path, 'w') as file:
        yaml.safe_dump(data, file)

    result = task_func(yaml_path, key)

    assert result == {'test_key': math.cos(1.0)}

    with open(yaml_path, 'r') as file:
        data = yaml.safe_load(file)

    assert data == {'test_key': math.cos(1.0)}