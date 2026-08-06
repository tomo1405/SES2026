import pytest
from src_1102 import task_func
import os
import tempfile
import shutil

@pytest.fixture
def test_directory():
    # Create a temporary directory for testing
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    # Clean up the temporary directory after tests
    shutil.rmtree(temp_dir)

def create_python_file(directory, filename, content):
    file_path = os.path.join(directory, filename)
    with open(file_path, 'w') as file:
        file.write(content)

def test_task_func_with_no_files(test_directory):
    # Test when there are no Python files in the directory
    result = task_func(test_directory)
    assert result == {}

def test_task_func_with_one_file(test_directory):
    # Test with one Python file that does nothing
    create_python_file(test_directory, 'test_script.py', 'print("Hello, World!")')
    result = task_func(test_directory)
    assert len(result) == 1
    assert 'test_script.py' in result
    assert isinstance(result['test_script.py'], float)

def test_task_func_with_multiple_files(test_directory):
    # Test with multiple Python files
    create_python_file(test_directory, 'script1.py', 'print("Script 1")')
    create_python_file(test_directory, 'script2.py', 'print("Script 2")')
    result = task_func(test_directory)
    assert len(result) == 2
    assert 'script1.py' in result
    assert 'script2.py' in result
    assert isinstance(result['script1.py'], float)
    assert isinstance(result['script2.py'], float)

def test_task_func_with_non_executable_file(test_directory):
    # Test with a non-executable file (e.g., a text file)
    create_python_file(test_directory, 'non_executable.txt', 'This is a text file.')
    result = task_func(test_directory)
    assert result == {}

def test_task_func_with_failing_script(test_directory):
    # Test with a script that raises an error
    create_python_file(test_directory, 'failing_script.py', 'raise ValueError("Test error")')
    result = task_func(test_directory)
    assert len(result) == 1
    assert 'failing_script.py' in result
    assert isinstance(result['failing_script.py'], float)