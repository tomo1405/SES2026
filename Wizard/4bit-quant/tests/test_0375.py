python
import pytest
from src_0375 import task_func

def test_task_func():
    # Test case 1: Directory does not exist
    with pytest.raises(FileNotFoundError):
        task_func('non_existent_directory/')

    # Test case 2: Directory exists, but no xlsx files
    with pytest.raises(FileNotFoundError):
        task_func('empty_directory/')

    # Test case 3: Directory exists, xlsx files exist, but no sheets
    with pytest.raises(ValueError):
        task_func('no_sheets/')

    # Test case 4: Directory exists, xlsx files exist, sheets exist, but no cells
    with pytest.raises(ValueError):
        task_func('no_cells/')

    # Test case 5: Directory exists, xlsx files exist, sheets exist, cells exist
    processed_files = task_func('valid_directory/')
    assert processed_files == 2