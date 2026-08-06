import pytest
from src_0564 import task_func
import os
import shutil
import tempfile

def test_task_func():
    # Create a temporary directory for the DLL files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a mock DLL file in the temporary directory
        dll_path = os.path.join(temp_dir, 'mock.dll')
        with open(dll_path, 'w') as f:
            f.write('Mock DLL content')

        # Create a destination directory
        dest_dir = os.path.join(temp_dir, 'destination')
        os.makedirs(dest_dir)

        # Call the function with the paths
        result = task_func(dll_path, dest_dir)

        # Check if the DLL file was moved to the destination directory
        assert os.path.exists(os.path.join(dest_dir, 'mock.dll'))
        assert not os.path.exists(dll_path)

        # Check if the function returned the correct library name
        assert result == 'mock.dll'

def test_task_func_no_dlls():
    # Create a temporary directory without any DLL files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a destination directory
        dest_dir = os.path.join(temp_dir, 'destination')
        os.makedirs(dest_dir)

        # Call the function with the paths
        result = task_func(os.path.join(temp_dir, 'nonexistent.dll'), dest_dir)

        # Check if the function returned the correct library name
        assert result == 'nonexistent.dll'

def test_task_func_multiple_dlls():
    # Create a temporary directory with multiple DLL files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create mock DLL files in the temporary directory
        dll_paths = [os.path.join(temp_dir, f'mock_{i}.dll') for i in range(3)]
        for dll_path in dll_paths:
            with open(dll_path, 'w') as f:
                f.write('Mock DLL content')

        # Create a destination directory
        dest_dir = os.path.join(temp_dir, 'destination')
        os.makedirs(dest_dir)

        # Call the function with the path of one of the DLLs
        result = task_func(dll_paths[0], dest_dir)

        # Check if all DLL files were moved to the destination directory
        for dll_path in dll_paths:
            assert os.path.exists(os.path.join(dest_dir, os.path.basename(dll_path)))
            assert not os.path.exists(dll_path)

        # Check if the function returned the correct library name
        assert result == 'mock_0.dll'