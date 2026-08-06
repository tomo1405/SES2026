import pytest
from src_0766 import task_func

@pytest.fixture
def setup():
    # Create a temporary directory for testing
    import tempfile
    import os
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    # Clean up the temporary directory after the test
    shutil.rmtree(temp_dir)

def test_task_func(setup):
    # Test case 1: Test with valid input
    from pathlib import Path
    import shutil
    import os

    # Create a sample file for testing
    source_file_path = "test_file.txt"
    with open(source_file_path, "w") as f:
        f.write("test content")

    # Call the function with the sample input
    result = task_func({"test_file.txt": "test content"}, target_dir=setup)

    # Assert the expected output
    assert os.path.exists(os.path.join(setup, "test_file.txt"))
    assert len(result) == 1

    # Clean up the test file
    os.remove(source_file_path)