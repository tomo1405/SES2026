import pytest
from src_0674 import task_func
import os
import shutil

@pytest.fixture
def temp_directory(tmpdir):
    """Create a temporary directory for testing."""
    return tmpdir.mkdir("test_dir")

def test_task_func_creates_directory(temp_directory):
    """Test that the directory is created if it doesn't exist."""
    task_func(str(temp_directory), 1)
    assert os.path.exists(str(temp_directory))

def test_task_func_creates_files(temp_directory):
    """Test that the correct number of files are created."""
    n_files = 5
    task_func(str(temp_directory), n_files)
    files = [f for f in os.listdir(str(temp_directory)) if os.path.isfile(os.path.join(str(temp_directory), f))]
    assert len(files) == n_files

def test_task_func_file_contents(temp_directory):
    """Test that each file contains a single digit."""
    n_files = 3
    task_func(str(temp_directory), n_files)
    for i in range(1, n_files + 1):
        with open(os.path.join(str(temp_directory), f"file_{i}.txt"), 'r') as file:
            content = file.read()
            assert content.isdigit() and 0 <= int(content) <= 9

def test_task_func_returns_correct_value(temp_directory):
    """Test that the function returns the correct number of files."""
    n_files = 7
    result = task_func(str(temp_directory), n_files)
    assert result == n_files

def test_task_func_overwrites_existing_files(temp_directory):
    """Test that existing files are overwritten."""
    n_files = 2
    task_func(str(temp_directory), n_files)
    initial_files = set(os.listdir(str(temp_directory)))

    # Write something different to the files
    for i in range(1, n_files + 1):
        with open(os.path.join(str(temp_directory), f"file_{i}.txt"), 'w') as file:
            file.write('9')

    task_func(str(temp_directory), n_files)
    final_files = set(os.listdir(str(temp_directory)))
    assert initial_files == final_files

    for i in range(1, n_files + 1):
        with open(os.path.join(str(temp_directory), f"file_{i}.txt"), 'r') as file:
            content = file.read()
            assert content.isdigit() and 0 <= int(content) <= 9

def test_task_func_with_zero_files(temp_directory):
    """Test that no files are created when n_files is 0."""
    task_func(str(temp_directory), 0)
    files = [f for f in os.listdir(str(temp_directory)) if os.path.isfile(os.path.join(str(temp_directory), f))]
    assert len(files) == 0

def test_task_func_with_negative_files(temp_directory):
    """Test that no files are created when n_files is negative."""
    task_func(str(temp_directory), -3)
    files = [f for f in os.listdir(str(temp_directory)) if os.path.isfile(os.path.join(str(temp_directory), f))]
    assert len(files) == 0

def test_task_func_with_existing_directory(temp_directory):
    """Test that the function works correctly with an existing directory."""
    os.makedirs(str(temp_directory))
    n_files = 4
    task_func(str(temp_directory), n_files)
    files = [f for f in os.listdir(str(temp_directory)) if os.path.isfile(os.path.join(str(temp_directory), f))]
    assert len(files) == n_files

def teardown_function():
    """Cleanup any temporary directories after tests."""
    temp_dir = "test_dir"
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)