import pytest
from src_0726 import task_func
import os
import glob
import tempfile
import codecs

@pytest.fixture
def setup_files(tmpdir):
    # Create temporary directory and files
    temp_dir = tmpdir.mkdir('temp_files')
    temp_dir.join('file1.txt').write('Привет мир', encoding='cp1251')
    temp_dir.join('file2.txt').write('Hello world', encoding='cp1251')
    return str(temp_dir)

def test_task_func(setup_files):
    # Run the function
    task_func(directory=setup_files, from_encoding='cp1251', to_encoding='utf8')

    # Check if the files have been converted correctly
    for filename in glob.glob(os.path.join(setup_files, '*.txt')):
        with codecs.open(filename, 'r', 'utf8') as file:
            content = file.read()
            assert isinstance(content, str), f"Content of {filename} is not a string"
            assert len(content) > 0, f"Content of {filename} is empty"

def test_no_files(setup_files):
    # Remove all files from the directory
    for filename in glob.glob(os.path.join(setup_files, '*.txt')):
        os.remove(filename)

    # Run the function
    task_func(directory=setup_files, from_encoding='cp1251', to_encoding='utf8')

    # Check if no files were processed
    assert len(glob.glob(os.path.join(setup_files, '*.txt'))) == 0, "Files were processed when none were present"

def test_nonexistent_directory():
    # Run the function with a non-existent directory
    with pytest.raises(FileNotFoundError):
        task_func(directory='./nonexistent_directory', from_encoding='cp1251', to_encoding='utf8')