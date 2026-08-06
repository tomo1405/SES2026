import re
import os
import glob
import pytest

def task_func(dir_path):

    if not os.path.isdir(dir_path):
        raise ValueError("Specified directory does not exist.")

    result = {}
    file_paths = glob.glob(f'{dir_path}/**/*.txt', recursive=True)
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            content = file.read()
        matches = re.findall(r'\berror\b', content, re.IGNORECASE)
        # Always set the file's count in the result dictionary, even if it's 0
        result[os.path.relpath(file_path, dir_path)] = len(matches)

    return result

def test_task_func():
    test_dir = "/path/to/test/directory"
    expected_result = {
        "file1.txt": 1,
        "file2.txt": 0,
        "subdirectory/file3.txt": 2,
    }
    with pytest.raises(ValueError):
        task_func("/invalid/directory")
    assert task_func(test_dir) == expected_result