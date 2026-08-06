import pytest
from src_0314 import task_func
import os
import shutil
from datetime import datetime

@pytest.fixture
def setup_test_directory(tmpdir):
    # Create a temporary directory and some test files
    test_dir = tmpdir.mkdir("test_dir")
    test_file1 = test_dir.join("file1.txt")
    test_file2 = test_dir.join("file2.txt")
    
    # Write some content to the files
    test_file1.write("prefix [content]")
    test_file2.write("another_prefix [more content]")
    
    yield str(test_dir)
    
    # Clean up the temporary directory after the test
    shutil.rmtree(str(test_dir))

def test_task_func(setup_test_directory):
    directory = setup_test_directory
    result_directory, moved_files = task_func(directory)
    
    # Check if the result directory is the same as the input directory
    assert result_directory == directory
    
    # Check if the files were moved to the correct subdirectories
    assert "prefix" in moved_files
    assert "another_prefix" in moved_files
    
    # Check if the filenames have the correct format
    for subdirectory, filenames in moved_files.items():
        for filename in filenames:
            assert re.match(r'.*_[0-9]{14}\.[a-zA-Z]+', filename)
    
    # Check if the files actually exist in the subdirectories
    for subdirectory, filenames in moved_files.items():
        subdirectory_path = os.path.join(directory, subdirectory)
        for filename in filenames:
            assert os.path.exists(os.path.join(subdirectory_path, filename))

def test_task_func_no_match(setup_test_directory):
    # Modify one of the files to not match the pattern
    test_file = os.path.join(setup_test_directory, "file1.txt")
    with open(test_file, 'w') as file:
        file.write("no match here")
    
    directory = setup_test_directory
    result_directory, moved_files = task_func(directory)
    
    # Check if no files were moved
    assert moved_files == {}

def test_task_func_empty_directory(setup_test_directory):
    # Remove all files from the directory
    for filename in os.listdir(setup_test_directory):
        os.remove(os.path.join(setup_test_directory, filename))
    
    directory = setup_test_directory
    result_directory, moved_files = task_func(directory)
    
    # Check if no files were moved
    assert moved_files == {}