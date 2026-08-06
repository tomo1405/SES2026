import pytest
from src_0676 import task_func
import os
import shutil

@pytest.fixture
def temp_directory(tmpdir):
    return tmpdir.mkdir("test_dir")

def test_task_func_creates_directory(temp_directory):
    directory = str(temp_directory)
    n_files = 3
    result = task_func(directory, n_files)
    assert os.path.exists(result)

def test_task_func_creates_correct_number_of_files(temp_directory):
    directory = str(temp_directory)
    n_files = 5
    task_func(directory, n_files)
    files = os.listdir(directory)
    assert len(files) == n_files

def test_task_func_files_contain_random_numbers(temp_directory):
    directory = str(temp_directory)
    n_files = 2
    task_func(directory, n_files)
    for i in range(n_files):
        filename = os.path.join(directory, f"file_{i+1}.txt")
        with open(filename, 'r') as file:
            content = file.read()
            assert content.isdigit() and 1 <= int(content) <= 100

def test_task_func_overwrites_existing_directory(temp_directory):
    directory = str(temp_directory)
    n_files = 1
    task_func(directory, n_files)
    with open(os.path.join(directory, "file_1.txt"), 'w') as file:
        file.write("existing_content")
    task_func(directory, n_files)
    with open(os.path.join(directory, "file_1.txt"), 'r') as file:
        content = file.read()
        assert content.isdigit() and 1 <= int(content) <= 100

@pytest.fixture(autouse=True)
def cleanup(request, temp_directory):
    def remove_temp_directory():
        shutil.rmtree(temp_directory)
    request.addfinalizer(remove_temp_directory)