import pytest
from src_0811 import task_func

def test_task_func():
    # Test case 1: execute_files=True
    results = task_func('path/to/dir', '*.exe', execute_files=True)
    assert len(results) == 2
    assert results[0] == 'output of file 1'
    assert results[1] == 'output of file 2'

    # Test case 2: execute_files=False
    results = task_func('path/to/dir', '*.exe', execute_files=False)
    assert len(results) == 2
    assert results[0] == 'path/to/dir/file1.exe'
    assert results[1] == 'path/to/dir/file2.exe'

    # Test case 3: no files found
    results = task_func('path/to/dir', '*.txt', execute_files=True)
    assert len(results) == 0

    # Test case 4: invalid directory path
    with pytest.raises(FileNotFoundError):
        task_func('path/to/invalid/dir', '*.exe', execute_files=True)