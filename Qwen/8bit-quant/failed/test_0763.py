import pytest
from src_0763 import task_func
import os
import zipfile

def test_task_func_default_parameters():
    # Test with default parameters
    result = task_func()
    assert os.path.exists(result)
    assert zipfile.is_zipfile(result)
    with zipfile.ZipFile(result, 'r') as zip_ref:
        file_list = zip_ref.namelist()
        assert len(file_list) == 3
        for file_name in ['file1.txt', 'file2.txt', 'file3.txt']:
            assert file_name in file_list
            with zip_ref.open(file_name) as file:
                content = file.read().decode('latin-1')
                assert content == 'Sopetón'

def test_task_func_custom_parameters():
    # Test with custom parameters
    directory_name = "custom_dir"
    content = "Custom Content"
    file_names = ["a.txt", "b.txt"]
    encoding = "utf-8"
    result = task_func(directory_name, content, file_names, encoding)
    assert os.path.exists(result)
    assert zipfile.is_zipfile(result)
    with zipfile.ZipFile(result, 'r') as zip_ref:
        file_list = zip_ref.namelist()
        assert len(file_list) == 2
        for file_name in file_names:
            assert file_name in file_list
            with zip_ref.open(file_name) as file:
                content = file.read().decode(encoding)
                assert content == "Custom Content"

def test_task_func_existing_directory():
    # Test with an existing directory
    directory_name = "existing_dir"
    os.makedirs(directory_name, exist_ok=True)
    result = task_func(directory_name)
    assert os.path.exists(result)
    assert zipfile.is_zipfile(result)
    with zipfile.ZipFile(result, 'r') as zip_ref:
        file_list = zip_ref.namelist()
        assert len(file_list) == 3
        for file_name in ['file1.txt', 'file2.txt', 'file3.txt']:
            assert file_name in file_list
            with zip_ref.open(file_name) as file:
                content = file.read().decode('latin-1')
                assert content == 'Sopetón'

def test_task_func_no_files():
    # Test with no files
    directory_name = "no_files_dir"
    file_names = []
    result = task_func(directory_name, file_names=file_names)
    assert os.path.exists(result)
    assert zipfile.is_zipfile(result)
    with zipfile.ZipFile(result, 'r') as zip_ref:
        file_list = zip_ref.namelist()
        assert len(file_list) == 0

def teardown_function():
    # Clean up created directories and files
    for dir_name in ["latin_files", "custom_dir", "existing_dir", "no_files_dir"]:
        if os.path.exists(dir_name):
            for root, dirs, files in os.walk(dir_name, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(dir_name)
    for zip_file in ["latin_files.zip", "custom_dir.zip", "existing_dir.zip", "no_files_dir.zip"]:
        if os.path.exists(zip_file):
            os.remove(zip_file)