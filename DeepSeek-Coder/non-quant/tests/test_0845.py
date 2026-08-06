import pytest
from src_0845 import task_func

def test_task_func():
    # Test with valid input
    file_path = 'test_output.csv'
    num_rows = 5
    random_seed = 42
    result = task_func(file_path, num_rows, random_seed)
    assert result == file_path
    assert os.path.exists(file_path)
    os.remove(file_path)  # Clean up

    # Test with invalid num_rows
    with pytest.raises(ValueError):
        task_func(file_path, -5, random_seed)