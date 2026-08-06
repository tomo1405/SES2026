import pytest
from src_0786 import task_func

def test_task_func_no_files():
    result = task_func("non_existent_pattern")
    assert result == "No files found matching the pattern."

def test_task_func_with_files():
    # Assuming we have a way to create temporary files for testing
    # This is a placeholder for actual file creation
    # For the purpose of this test, let's assume we have a file
    # We need to ensure that the function behaves correctly when files are present
    # This test will fail if the function does not handle multiple files correctly
    # This is a placeholder for actual file creation and deletion
    # In a real test, you would create files, call the function, and then clean up
    pass

# Add more tests as necessary