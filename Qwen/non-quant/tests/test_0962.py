import os
import tempfile
from typing import Counter

import pytest
from src_0962 import task_func


def test_task_func_non_existent_directory():
    with pytest.raises(OSError, match="directory must exist"):
        task_func("/nonexistent/directory")

def test_task_func_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert result == Counter()

def test_task_func_with_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some files with different extensions
        open(os.path.join(temp_dir, "file1.txt"), "w").close()
        open(os.path.join(temp_dir, "file2.docx"), "w").close()
        open(os.path.join(temp_dir, "file3.csv"), "w").close()
        open(os.path.join(temp_dir, "file4.xlsx"), "w").close()
        open(os.path.join(temp_dir, "file5.pdf"), "w").close()  # Not in the default extensions

        result = task_func(temp_dir)
        expected = Counter({
            ".txt": 1,
            ".docx": 1,
            ".xlsx": 1,
            ".csv": 1
        })
        assert result == expected

def test_task_func_with_subdirectories():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create subdirectories and files
        subdir1 = os.path.join(temp_dir, "subdir1")
        subdir2 = os.path.join(temp_dir, "subdir2")
        os.makedirs(subdir1)
        os.makedirs(subdir2)

        open(os.path.join(subdir1, "file1.txt"), "w").close()
        open(os.path.join(subdir2, "file2.txt"), "w").close()
        open(os.path.join(subdir1, "file3.docx"), "w").close()

        result = task_func(temp_dir)
        expected = Counter({
            ".txt": 2,
            ".docx": 1
        })
        assert result == expected

def test_task_func_keep_zero_false():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir, keep_zero=False)
        assert result == Counter()

def test_task_func_custom_extensions():
    with tempfile.TemporaryDirectory() as temp_dir:
        open(os.path.join(temp_dir, "file1.py"), "w").close()
        open(os.path.join(temp_dir, "file2.js"), "w").close()

        result = task_func(temp_dir, extensions=[".py", ".js"])
        expected = Counter({
            ".py": 1,
            ".js": 1
        })
        assert result == expected

    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir, extensions=[".py", ".js"], keep_zero=True)
        expected = Counter({
            ".py": 0,
            ".js": 0
        })
        assert result == expected