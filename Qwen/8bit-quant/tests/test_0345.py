import pytest
from src_0345 import task_func
import os
import shutil
import tempfile

def test_task_func_success():
    with tempfile.TemporaryDirectory() as src_folder:
        with tempfile.TemporaryDirectory() as backup_dir:
            # Create some files in the source folder
            file_path = os.path.join(src_folder, 'test_file.txt')
            with open(file_path, 'w') as f:
                f.write('Hello, World!')
            
            # Call the function
            result = task_func(src_folder, backup_dir)
            
            # Check if the result is True
            assert result is True
            
            # Check if the source folder is deleted
            assert not os.path.exists(src_folder)
            
            # Check if the backup folder is created and contains the same files
            backup_folder = os.path.join(backup_dir, os.path.basename(src_folder))
            assert os.path.isdir(backup_folder)
            backup_file_path = os.path.join(backup_folder, 'test_file.txt')
            assert os.path.isfile(backup_file_path)
            with open(backup_file_path, 'r') as f:
                content = f.read()
                assert content == 'Hello, World!'

def test_task_func_source_folder_not_exists():
    with tempfile.TemporaryDirectory() as backup_dir:
        # Call the function with a non-existing source folder
        with pytest.raises(ValueError) as excinfo:
            task_func('/non/existing/folder', backup_dir)
        
        # Check the error message
        assert str(excinfo.value) == "Source folder '/non/existing/folder' does not exist."

def test_task_func_delete_failure():
    with tempfile.TemporaryDirectory() as src_folder:
        with tempfile.TemporaryDirectory() as backup_dir:
            # Make the source folder read-only
            os.chmod(src_folder, 0o444)
            
            # Call the function
            result = task_func(src_folder, backup_dir)
            
            # Check if the result is False
            assert result is False
            
            # Check if the source folder still exists
            assert os.path.exists(src_folder)
            
            # Check if the backup folder is created
            backup_folder = os.path.join(backup_dir, os.path.basename(src_folder))
            assert not os.path.exists(backup_folder)