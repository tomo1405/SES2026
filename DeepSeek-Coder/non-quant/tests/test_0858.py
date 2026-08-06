import pytest
from src_0858 import task_func
import os
import shutil
import glob
import time

@pytest.fixture
def setup_and_teardown():
    # Setup code here
    yield
    # Teardown code here

def test_task_func(setup_and_teardown):
    # Test cases here
    SOURCE_DIR = "test_source_dir"
    DEST_DIR = "test_dest_dir"
    EXTENSIONS = [".txt"]
    os.makedirs(SOURCE_DIR, exist_ok=True)
    os.makedirs(DEST_DIR, exist_ok=True)

    # Add test files
    with open(os.path.join(SOURCE_DIR, "testfile1.txt"), "w") as f:
        f.write("test content")

    result = task_func(SOURCE_DIR, DEST_DIR, EXTENSIONS)

    assert len(os.listdir(SOURCE_DIR)) == 0
    assert len(os.listdir(DEST_DIR)) == 1
    assert "testfile1.txt" in os.listdir(DEST_DIR)
    assert result == ["testfile1.txt"]

    # Clean up
    shutil.rmtree(SOURCE_DIR)
    shutil.rmtree(DEST_DIR)