import pytest
from src_0769 import task_func

def test_task_func():
    # Test case 1: directory does not exist
    with pytest.raises(ValueError):
        task_func('invalid_dir')

    # Test case 2: directory exists but no files
    with pytest.raises(ValueError):
        task_func('tests/test_data/empty_dir')

    # Test case 3: directory exists and files exist
    result = task_func('tests/test_data/valid_dir')
    assert result == {'file1.txt': 2, 'file2.txt': 1}

    # Test case 4: directory exists and files exist, but no matches
    result = task_func('tests/test_data/no_matches')
    assert result == {'file1.txt': 0, 'file2.txt': 0}