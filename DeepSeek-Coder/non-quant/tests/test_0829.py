import pytest
from src_0829 import task_func
import os
import shutil
import errno

@pytest.fixture
def setup_and_teardown():
    # Setup code before each test
    test_filename = "test_file.txt"
    test_dest_dir = "test_dest_dir"
    os.makedirs(test_dest_dir, exist_ok=True)
    with open(test_filename, 'w') as f:
        f.write("Test content")
    yield test_filename, test_dest_dir
    # Teardown code after each test
    os.remove(test_filename)
    shutil.rmtree(test_dest_dir)

@pytest.mark.parametrize("filename, dest_dir", [
    ("test_file.txt", "test_dest_dir")
])
def test_task_func(setup_and_teardown, filename, dest_dir):
    result = task_func(filename, dest_dir)
    assert os.path.exists(result)
    assert os.path.isdir(result)
    assert os.path.isfile(os.path.join(result, os.path.basename(filename)))