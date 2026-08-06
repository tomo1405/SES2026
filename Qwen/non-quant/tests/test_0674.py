import pytest
from src_0674 import task_func
import os
import tempfile

def test_task_func():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Test with 5 files
        result = task_func(temp_dir, 5)
        assert result == 5

        # Check if all 5 files exist
        for i in range(5):
            filename = os.path.join(temp_dir, f"file_{i+1}.txt")
            assert os.path.exists(filename)

        # Check file contents
        for i in range(5):
            filename = os.path.join(temp_dir, f"file_{i+1}.txt")
            with open(filename, 'r') as file:
                content = file.read()
                assert content.isdigit()

# Test with 0 files
def test_task_func_zero_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir, 0)
        assert result == 0
        assert len(os.listdir(temp_dir)) == 0

# Test with negative number of files
def test_task_func_negative_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        with pytest.raises(ValueError):
            task_func(temp_dir, -1)

# Test with non-existent directory
def test_task_func_non_existent_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        non_existent_dir = os.path.join(temp_dir, "non_existent")
        result = task_func(non_existent_dir, 3)
        assert result == 3
        assert os.path.exists(non_existent_dir)
        assert len(os.listdir(non_existent_dir)) == 3