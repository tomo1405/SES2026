python
import os
import re
import pytest

def task_func(pattern: str, replacement: str, directory: str) -> bool:
    try:
        for file in os.listdir(directory):
            if re.search(pattern, file):
                new_filename = re.sub(pattern, replacement, file)
                os.rename(os.path.join(directory, file), os.path.join(directory, new_filename))
        return True
    except Exception as e:
        return False

def test_task_func():
    assert task_func('test', 'new', '.') == True
    assert task_func('test', 'new', 'nonexistent_dir') == False