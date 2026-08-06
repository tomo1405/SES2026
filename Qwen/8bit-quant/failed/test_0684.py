import pytest
from src_0684 import task_func
import os
import tempfile
import yaml

@pytest.fixture
def temp_yaml_file():
    with tempfile.NamedTemporaryFile(delete=False, mode='w+') as temp_file:
        yaml_data = {'test_key': 1.0}
        yaml.dump(yaml_data, temp_file)
        temp_file.flush()
        yield temp_file.name
    os.remove(temp_file.name)

def test_task_func_existing_key(temp_yaml_file):
    result = task_func(temp_yaml_file, 'test_key')
    assert result['test_key'] == math.cos(1.0)

def test_task_func_non_existing_key(temp_yaml_file):
    result = task_func(temp_yaml_file, 'non_existent_key')
    assert 'non_existent_key' not in result

def test_task_func_with_empty_yaml(temp_yaml_file):
    with open(temp_yaml_file, 'w') as file:
        yaml.safe_dump({}, file)

    result = task_func(temp_yaml_file, 'empty_key')
    assert result == {}

def test_task_func_with_non_numeric_value(temp_yaml_file):
    with open(temp_yaml_file, 'w') as file:
        yaml.safe_dump({'test_key': 'string'}, file)

    result = task_func(temp_yaml_file, 'test_key')
    assert result['test_key'] == 'string'

def test_task_func_with_nested_keys(temp_yaml_file):
    with open(temp_yaml_file, 'w') as file:
        yaml.safe_dump({'outer': {'inner': 2.0}}, file)

    result = task_func(temp_yaml_file, 'outer.inner')
    assert result['outer']['inner'] == math.cos(2.0)