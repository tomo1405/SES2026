import pytest
from src_0756 import task_func
import os
import tempfile
import shutil

@pytest.fixture
def temp_dir():
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)

def test_task_func_with_files(temp_dir):
    # Create some files in the temporary directory
    file_paths = [
        os.path.join(temp_dir, 'file1.txt'),
        os.path.join(temp_dir, 'file2.docx'),
        os.path.join(temp_dir, 'file3.pdf')
    ]
    for file_path in file_paths:
        with open(file_path, 'w') as f:
            f.write('Test content')

    # Call the function
    result = task_func(temp_dir)

    # Check if the files have been renamed correctly
    expected_new_filenames = ['txt.file1', 'docx.file2', 'pdf.file3']
    assert result == expected_new_filenames

    # Check if the files exist with the new names
    for new_filename in expected_new_filenames:
        assert os.path.exists(os.path.join(temp_dir, new_filename))

def test_task_func_empty_directory(temp_dir):
    # Call the function on an empty directory
    result = task_func(temp_dir)

    # Check if the result is an empty list
    assert result == []

def test_task_func_nonexistent_directory():
    # Call the function with a non-existent directory path
    with pytest.raises(FileNotFoundError):
        task_func('/nonexistent/directory')