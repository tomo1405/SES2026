import os
import shutil
import string
import pytest
from src_0854 import task_func

INVALID_CHARACTERS = string.punctuation + string.whitespace

def test_task_func():
    directory_path = "/path/to/directory"
    summary = task_func(directory_path)
    assert isinstance(summary, dict)
    for key, value in summary.items():
        assert isinstance(key, str)
        assert isinstance(value, int)
    invalid_files = [filename for filename in os.listdir(directory_path) if any(char in INVALID_CHARACTERS for char in filename)]
    invalid_files_count = len(invalid_files)
    assert summary['Invalid'] == invalid_files_count
    for filename in invalid_files:
        assert os.path.exists(os.path.join(directory_path, 'Invalid', filename))
    other_files = [filename for filename in os.listdir(directory_path) if not any(char in INVALID_CHARACTERS for char in filename)]
    for filename in other_files:
        extension = os.path.splitext(filename)[-1].strip('.')
        assert os.path.exists(os.path.join(directory_path, extension, filename))