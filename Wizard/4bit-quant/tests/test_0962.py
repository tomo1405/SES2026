python
import os
import glob
from collections import Counter
import pytest

def task_func(directory, extensions=[".txt", ".docx", ".xlsx", ".csv"], keep_zero=True):
    if not os.path.exists(directory):
        raise OSError("directory must exist.")

    counter = Counter()

    for suffix in extensions:
        count = len(
            glob.glob(os.path.join(directory, "**", "*" + suffix), recursive=True)
        )
        if count:
            counter[suffix] += count
        else:
            if keep_zero:
                counter[suffix] += count
    return counter

def test_task_func():
    # Test case 1: directory does not exist
    with pytest.raises(OSError):
        task_func("nonexistent_directory")

    # Test case 2: directory exists but has no files with specified extensions
    assert task_func("tests/test_data/empty_dir") == Counter()

    # Test case 3: directory exists and has files with specified extensions
    assert task_func("tests/test_data/test_dir") == Counter({'.txt': 1, '.docx': 1, '.xlsx': 1, '.csv': 1})

    # Test case 4: directory exists and has files with specified extensions, but keep_zero is False
    assert task_func("tests/test_data/test_dir", keep_zero=False) == Counter({'.txt': 1, '.docx': 1, '.xlsx': 1, '.csv': 1})

    # Test case 5: directory exists and has files with specified extensions, but some extensions are missing
    assert task_func("tests/test_data/test_dir_missing_ext") == Counter({'.txt': 1, '.docx': 1, '.xlsx': 1, '.csv': 1})

    # Test case 6: directory exists and has files with specified extensions, but some extensions are missing, and keep_zero is False
    assert task_func("tests/test_data/test_dir_missing_ext", keep_zero=False) == Counter({'.txt': 1, '.docx': 1, '.xlsx': 1, '.csv': 1})