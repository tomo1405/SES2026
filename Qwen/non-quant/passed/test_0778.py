import pytest
from src_0778 import task_func
import os
import zipfile
import tempfile
import shutil

def create_temp_zip_file(directory, base_name, contents):
    zip_path = os.path.join(directory, f"{base_name}-123.zip")
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for name, data in contents.items():
            zipf.writestr(name, data)
    return zip_path

def test_task_func_with_single_zip_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        create_temp_zip_file(temp_dir, "test", {"file1.txt": "content1", "file2.txt": "content2"})
        result = task_func(temp_dir)
        assert len(result) == 1
        assert os.path.exists(os.path.join(temp_dir, "test"))
        assert os.path.exists(os.path.join(temp_dir, "test", "file1.txt"))
        assert os.path.exists(os.path.join(temp_dir, "test", "file2.txt"))

def test_task_func_with_multiple_zip_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        create_temp_zip_file(temp_dir, "test1", {"file1.txt": "content1"})
        create_temp_zip_file(temp_dir, "test2", {"file2.txt": "content2"})
        result = task_func(temp_dir)
        assert len(result) == 2
        assert os.path.exists(os.path.join(temp_dir, "test1"))
        assert os.path.exists(os.path.join(temp_dir, "test1", "file1.txt"))
        assert os.path.exists(os.path.join(temp_dir, "test2"))
        assert os.path.exists(os.path.join(temp_dir, "test2", "file2.txt"))

def test_task_func_with_no_matching_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        open(os.path.join(temp_dir, "nonmatchingfile.txt"), 'a').close()
        result = task_func(temp_dir)
        assert len(result) == 0

def test_task_func_with_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert len(result) == 0

def test_task_func_with_invalid_zip_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        invalid_zip_path = os.path.join(temp_dir, "invalid.zip")
        with open(invalid_zip_path, 'wb') as f:
            f.write(b"invalid content")
        result = task_func(temp_dir)
        assert len(result) == 0

def test_task_func_with_nonexistent_directory():
    with pytest.raises(FileNotFoundError):
        task_func("/nonexistent/directory")