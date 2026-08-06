python
import pytest
from src_0769 import task_func

def test_task_func():
    # Test case 1: Valid directory path
    result = task_func('tests/test_files')
    assert result == {'test_file.txt': 1, 'test_file2.txt': 0}

    # Test case 2: Invalid directory path
    with pytest.raises(ValueError):
        task_func('invalid_dir')

    # Test case 3: Directory path with no text files
    result = task_func('tests/empty_dir')
    assert result == {}