python
import pytest
from src_0684 import task_func

def test_task_func():
    # Test case 1: Valid input
    input_yaml_path = 'input.yaml'
    input_key = 'angle'
    input_data = {'angle': 30}
    expected_output_data = {'angle': 0.5}

    with open(input_yaml_path, 'w') as file:
        yaml.safe_dump(input_data, file)

    task_func(input_yaml_path, input_key)

    with open(input_yaml_path, 'r') as file:
        output_data = yaml.safe_load(file)

    assert output_data == expected_output_data

    # Test case 2: Invalid input (key not in data)
    input_yaml_path = 'input.yaml'
    input_key = 'invalid_key'
    input_data = {'angle': 30}
    expected_output_data = {'angle': 30}

    with open(input_yaml_path, 'w') as file:
        yaml.safe_dump(input_data, file)

    task_func(input_yaml_path, input_key)

    with open(input_yaml_path, 'r') as file:
        output_data = yaml.safe_load(file)

    assert output_data == expected_output_data

    # Test case 3: Invalid input (yaml_path does not exist)
    input_yaml_path = 'invalid_path.yaml'
    input_key = 'angle'
    input_data = {'angle': 30}
    expected_output_data = None

    with pytest.raises(FileNotFoundError):
        task_func(input_yaml_path, input_key)

    # Test case 4: Invalid input (yaml_path is a directory)
    input_yaml_path = '.'
    input_key = 'angle'
    input_data = {'angle': 30}
    expected_output_data = None

    with pytest.raises(IsADirectoryError):
        task_func(input_yaml_path, input_key)