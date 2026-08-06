import pytest
from src_0841 import task_func

def test_task_func():
    # Test with default parameters
    file_path = "test_output.csv"
    num_rows = 100
    result = task_func(file_path=file_path, num_rows=num_rows)
    assert result == file_path
    assert os.path.exists(file_path)
    os.remove(file_path)  # Clean up

    # Test with different parameters
    file_path = "test_output_2.csv"
    num_rows = 200
    result = task_func(file_path=file_path, num_rows=num_rows)
    assert result == file_path
    assert os.path.exists(file_path)
    os.remove(file_path)  # Clean up