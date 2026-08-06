import os
import re
import pytest
from src_0797 import task_func

@pytest.mark.parametrize("directory, expected_output", [
    ("/path/to/directory", ["path/to/directory/file1.txt", "path/to/directory/file2.txt"]),
    ("/another/path/to/directory", ["another/path/to/directory/file3.txt"]),
    ("/empty/directory", [])
])
def test_task_func(directory, expected_output):
    assert task_func(directory) == expected_output