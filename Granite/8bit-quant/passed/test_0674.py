import os
import random
import pytest
from src_0674 import task_func

def test_task_func():
    directory = "/tmp/test_directory"
    n_files = 5
    expected_output = n_files

    # Test when directory does not exist
    if not os.path.exists(directory):
        with pytest.raises(FileNotFoundError):
            task_func(directory, n_files)

    # Test when directory exists
    else:
        actual_output = task_func(directory, n_files)
        assert actual_output == expected_output