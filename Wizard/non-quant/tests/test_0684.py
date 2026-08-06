python
import pytest
from src_0684 import task_func

def test_task_func():
    # Test case 1: key exists in YAML file
    yaml_path = 'test.yaml'
    key = 'angle'
    data = {key: 30}
    with open(yaml_path, 'w') as file:
        yaml.safe_dump(data, file)
    task_func(yaml_path, key)
    with open(yaml_path, 'r') as file:
        data = yaml.safe_load(file)
    assert data[key] == pytest.approx(0.8660254037844386)

    # Test case 2: key does not exist in YAML file
    yaml_path = 'test.yaml'
    key = 'angle'
    data = {}
    with open(yaml_path, 'w') as file:
        yaml.safe_dump(data, file)
    task_func(yaml_path, key)
    with open(yaml_path, 'r') as file:
        data = yaml.safe_load(file)
    assert key not in data

    # Test case 3: key is None
    yaml_path = 'test.yaml'
    key = None
    data = {key: 30}
    with open(yaml_path, 'w') as file:
        yaml.safe_dump(data, file)
    task_func(yaml_path, key)
    with open(yaml_path, 'r') as file:
        data = yaml.safe_load(file)
    assert key not in data