python
import os
import glob
import re
import pytest

from src_0769 import task_func

def test_task_func():
    # Test case 1: Directory does not exist
    with pytest.raises(ValueError):
        task_func('nonexistent_dir')

    # Test case 2: Directory is empty
    result = task_func('tests/test_data/empty_dir')
    assert result == {}

    # Test case 3: Directory contains files with no errors
    result = task_func('tests/test_data/no_errors')
    assert result == {}

    # Test case 4: Directory contains files with errors
    result = task_func('tests/test_data/with_errors')
    assert result == {'file1.txt': 1, 'file2.txt': 2, 'subdir/file3.txt': 1}