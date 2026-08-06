import pytest
from src_0564 import task_func
import os
import shutil
import glob
import ctypes

@pytest.fixture
def setup():
    # Create a temporary directory and file for testing
    test_dir = 'test_dir'
    os.makedirs(test_dir, exist_ok=True)
    yield test_dir
    shutil.rmtree(test_dir)

def test_task_func(setup):
    # Create a dummy DLL file
    dll_content = b'\x7fELF'  # Dummy ELF content for the DLL
    dll_path = os.path.join(setup, 'test.dll')
    with open(dll_path, 'wb') as f:
        f.write(dll_content)

    # Call the function
    result = task_func(dll_path, setup)

    # Check the result
    assert result == 'test_lib'  # Assuming the library name is 'test_lib'
    assert os.path.exists(os.path.join(setup, 'test.dll'))