import re
import os
import shutil
import pytest
from src_0390 import task_func

def test_task_func():
    directory = "/path/to/directory"
    pattern = re.compile(r'(like|what)', re.IGNORECASE)
    interesting_files = [file for file in os.listdir(directory) if pattern.search(file)]

    # Test if the directory for interesting files exists
    assert os.path.exists(os.path.join(directory, 'Interesting Files'))

    # Test if the interesting files are moved to the new directory
    for file in interesting_files:
        assert not os.path.exists(os.path.join(directory, file))
        assert os.path.exists(os.path.join(directory, 'Interesting Files', file))

    # Test if the function returns the correct value
    assert task_func(directory) == interesting_files