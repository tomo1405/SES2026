import pytest
from src_1129 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    file_path = 'test_data.json'
    unknown_key = 'example_key'
    with open(file_path, 'w') as f:
        json.dump({'A': {unknown_key: {"maindata": [{"Info": "test_value"}]}}, f)
    
    result = task_func(file_path, unknown_key)
    assert os.path.exists(result)
    with open(result, 'r') as f:
        assert f.read() == 'test_value'
    os.remove(result)

    # Add more test cases as needed