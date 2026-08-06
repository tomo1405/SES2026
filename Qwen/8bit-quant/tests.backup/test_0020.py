import pytest
from src_0020 import task_func
import os
import tempfile

def test_task_func_directory_not_found():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func('/nonexistent/directory')
    assert str(excinfo.value) == "Directory '/nonexistent/directory' not found."

def test_task_func_no_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert result is None

def test_task_func_files_present():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some files in the temporary directory
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')
        with open(file1_path, 'w') as f:
            f.write('content1')
        with open(file2_path, 'w') as f:
            f.write('content2')
        
        result = task_func(temp_dir)
        assert result == os.path.join(temp_dir, 'files.zip')
        
        # Check if the zip file contains the correct files
        with zipfile.ZipFile(result, 'r') as zipf:
            zip_contents = zipf.namelist()
            assert sorted(zip_contents) == ['file1.txt', 'file2.txt']

def test_task_func_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert result is None