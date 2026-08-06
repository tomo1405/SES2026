import pytest
from src_0763 import task_func
import os
import zipfile

def test_task_func_default_params():
    # Test with default parameters
    result = task_func()
    assert result == "latin_files.zip"
    assert os.path.exists("latin_files")
    assert os.path.exists(result)
    with zipfile.ZipFile(result, 'r') as zipf:
        assert len(zipf.namelist()) == 3
        for file in ['file1.txt', 'file2.txt', 'file3.txt']:
            assert file in zipf.namelist()
            with zipf.open(file) as f:
                content = f.read().decode('latin-1')
                assert content == 'Sopetón'

def test_task_func_custom_params():
    # Test with custom parameters
    directory_name = "custom_dir"
    content = "TestContent"
    file_names = ['test1.txt', 'test2.txt']
    encoding = "utf-8"
    result = task_func(directory_name, content, file_names, encoding)
    assert result == f"{directory_name}.zip"
    assert os.path.exists(directory_name)
    assert os.path.exists(result)
    with zipfile.ZipFile(result, 'r') as zipf:
        assert len(zipf.namelist()) == 2
        for file in file_names:
            assert file in zipf.namelist()
            with zipf.open(file) as f:
                content = f.read().decode(encoding)
                assert content == 'TestContent'

def test_task_func_empty_directory():
    # Test with empty directory
    directory_name = "empty_dir"
    file_names = []
    result = task_func(directory_name, file_names=file_names)
    assert result == f"{directory_name}.zip"
    assert os.path.exists(directory_name)
    assert os.path.exists(result)
    with zipfile.ZipFile(result, 'r') as zipf:
        assert len(zipf.namelist()) == 0

def test_task_func_cleanup():
    # Test cleanup after running the function
    directory_name = "cleanup_test"
    result = task_func(directory_name)
    assert os.path.exists(result)
    assert os.path.exists(directory_name)
    task_func(directory_name, cleanup=True)
    assert not os.path.exists(directory_name)
    assert not os.path.exists(result)

def test_task_func_nonexistent_directory():
    # Test with a non-existent directory
    directory_name = "nonexistent_dir"
    result = task_func(directory_name)
    assert result == f"{directory_name}.zip"
    assert os.path.exists(directory_name)
    assert os.path.exists(result)