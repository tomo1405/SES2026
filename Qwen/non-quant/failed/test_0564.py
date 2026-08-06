import pytest
from src_0564 import task_func
import os
import shutil
import tempfile

@pytest.fixture
def setup_files():
    temp_dir = tempfile.mkdtemp()
    dll_files = [os.path.join(temp_dir, f'dll_{i}.dll') for i in range(3)]
    for dll_file in dll_files:
        with open(dll_file, 'w') as f:
            f.write('')
    yield dll_files, temp_dir
    shutil.rmtree(temp_dir)

def test_task_func(setup_files):
    dll_files, temp_dir = setup_files
    destination_dir = tempfile.mkdtemp()

    # Create a dummy .so file to simulate the library
    lib_path = os.path.join(temp_dir, 'lib.so')
    with open(lib_path, 'w') as f:
        f.write('')

    result = task_func(lib_path, destination_dir)

    # Check if the DLL files have been moved to the destination directory
    assert all(os.path.exists(os.path.join(destination_dir, os.path.basename(dll_file))) for dll_file in dll_files)

    # Check if the function returns the correct library name
    assert result == 'lib.so'

    shutil.rmtree(destination_dir)