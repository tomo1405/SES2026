import pytest
from src_0726 import task_func
import os
import glob
import tempfile
import shutil

# Constants
DIRECTORY_PATH = './files/'

@pytest.fixture
def setup_files(tmpdir):
    # Create a temporary directory and some sample files
    temp_dir = tmpdir.mkdir("temp_files")
    test_files = [
        temp_dir.join("file1.txt"),
        temp_dir.join("file2.txt"),
        temp_dir.join("file3.txt")
    ]
    for file in test_files:
        file.write("Hello, world!", encoding='cp1251')
    
    return str(temp_dir)

def test_task_func(setup_files):
    task_func(directory=setup_files, from_encoding='cp1251', to_encoding='utf8')

    # Check if all files have been encoded to utf8
    for filename in glob.glob(os.path.join(setup_files, '*.txt')):
        with open(filename, 'r', encoding='utf8') as file:
            content = file.read()
            assert content == "Hello, world!"

def test_task_func_nonexistent_directory():
    # Test with a non-existent directory
    with pytest.raises(FileNotFoundError):
        task_func(directory='./non_existent_directory/', from_encoding='cp1251', to_encoding='utf8')

def test_task_func_no_files():
    # Test with an empty directory
    with tempfile.TemporaryDirectory() as temp_dir:
        task_func(directory=temp_dir, from_encoding='cp1251', to_encoding='utf8')
        assert len(os.listdir(temp_dir)) == 0