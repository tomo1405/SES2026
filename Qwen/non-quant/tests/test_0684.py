import math

import pytest
import yaml
from src_0684 import task_func


@pytest.fixture
def create_temp_yaml_file(tmpdir):
    content = {
        'test_key': 1.0,
        'another_key': 'value'
    }
    file_path = tmpdir.join('temp.yaml')
    with open(file_path, 'w') as file:
        yaml.safe_dump(content, file)
    return str(file_path)

def test_task_func_updates_value(create_temp_yaml_file):
    yaml_path = create_temp_yaml_file
    key = 'test_key'
    expected_value = math.cos(1.0)
    
    result = task_func(yaml_path, key)
    
    assert result[key] == expected_value
    
    with open(yaml_path, 'r') as file:
        updated_data = yaml.safe_load(file)
    
    assert updated_data[key] == expected_value

def test_task_func_does_not_update_nonexistent_key(create_temp_yaml_file):
    yaml_path = create_temp_yaml_file
    key = 'nonexistent_key'
    
    result = task_func(yaml_path, key)
    
    assert key not in result
    
    with open(yaml_path, 'r') as file:
        updated_data = yaml.safe_load(file)
    
    assert key not in updated_data

def test_task_func_handles_empty_yaml(create_temp_yaml_file):
    yaml_path = create_temp_yaml_file
    with open(yaml_path, 'w') as file:
        yaml.safe_dump({}, file)
    
    key = 'test_key'
    result = task_func(yaml_path, key)
    
    assert key not in result
    
    with open(yaml_path, 'r') as file:
        updated_data = yaml.safe_load(file)
    
    assert key not in updated_data

def test_task_func_preserves_other_keys(create_temp_yaml_file):
    yaml_path = create_temp_yaml_file
    key = 'test_key'
    expected_value = math.cos(1.0)
    
    result = task_func(yaml_path, key)
    
    assert 'another_key' in result and result['another_key'] == 'value'
    
    with open(yaml_path, 'r') as file:
        updated_data = yaml.safe_load(file)
    
    assert 'another_key' in updated_data and updated_data['another_key'] == 'value'