import pytest
from src_0381 import task_func
import os
import shutil
import tempfile

@pytest.fixture
def temp_dir():
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)

def test_task_func_with_files(temp_dir):
    # Create some files in the temporary directory
    file_paths = [
        os.path.join(temp_dir, 'file1.txt'),
        os.path.join(temp_dir, 'file2.jpg'),
        os.path.join(temp_dir, 'file3.pdf')
    ]
    for file_path in file_paths:
        with open(file_path, 'w') as f:
            f.write('test content')

    # Run the function
    task_func(temp_dir)

    # Check that the files have been moved to the correct directories
    assert os.path.exists(os.path.join(temp_dir, 'txt'))
    assert os.path.exists(os.path.join(temp_dir, 'jpg'))
    assert os.path.exists(os.path.join(temp_dir, 'pdf'))

    assert len(os.listdir(os.path.join(temp_dir, 'txt'))) == 1
    assert len(os.listdir(os.path.join(temp_dir, 'jpg'))) == 1
    assert len(os.listdir(os.path.join(temp_dir, 'pdf'))) == 1

def test_task_func_with_no_files(temp_dir):
    # Run the function on an empty directory
    task_func(temp_dir)

    # Check that no directories were created
    assert len(os.listdir(temp_dir)) == 0

def test_task_func_with_hidden_files(temp_dir):
    # Create a hidden file in the temporary directory
    hidden_file_path = os.path.join(temp_dir, '.hiddenfile')
    with open(hidden_file_path, 'w') as f:
        f.write('hidden content')

    # Run the function
    task_func(temp_dir)

    # Check that the hidden file was not moved
    assert os.path.exists(hidden_file_path)
    assert len(os.listdir(temp_dir)) == 1

def test_task_func_with_directory(temp_dir):
    # Create a subdirectory in the temporary directory
    sub_dir_path = os.path.join(temp_dir, 'subdir')
    os.mkdir(sub_dir_path)

    # Run the function
    task_func(temp_dir)

    # Check that the subdirectory was not moved
    assert os.path.exists(sub_dir_path)
    assert len(os.listdir(temp_dir)) == 1