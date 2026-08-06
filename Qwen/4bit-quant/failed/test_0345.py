import pytest
from src_0345 import task_func
import os
import tempfile

def test_task_func_success():
    # Create a temporary directory and some files in it
    with tempfile.TemporaryDirectory() as src_folder:
        with open(os.path.join(src_folder, 'file1.txt'), 'w') as f:
            f.write('content1')
        with open(os.path.join(src_folder, 'file2.txt'), 'w') as f:
            f.write('content2')

        # Create a temporary backup directory
        with tempfile.TemporaryDirectory() as backup_dir:
            result = task_func(src_folder, backup_dir)

            # Check if the source folder is deleted
            assert not os.path.exists(src_folder)

            # Check if the backup folder exists and contains the same files
            backup_folder = os.path.join(backup_dir, os.path.basename(src_folder))
            assert os.path.isdir(backup_folder)
            assert set(os.listdir(backup_folder)) == {'file1.txt', 'file2.txt'}
            with open(os.path.join(backup_folder, 'file1.txt'), 'r') as f:
                assert f.read() == 'content1'
            with open(os.path.join(backup_folder, 'file2.txt'), 'r') as f:
                assert f.read() == 'content2'

            # Check if the function returned True
            assert result is True

def test_task_func_source_folder_not_exists():
    # Create a temporary backup directory
    with tempfile.TemporaryDirectory() as backup_dir:
        src_folder = 'non_existent_folder'
        with pytest.raises(ValueError) as excinfo:
            task_func(src_folder, backup_dir)
        assert str(excinfo.value) == f"Source folder '{src_folder}' does not exist."

def test_task_func_delete_error():
    # Create a temporary directory and some files in it
    with tempfile.TemporaryDirectory() as src_folder:
        with open(os.path.join(src_folder, 'file1.txt'), 'w') as f:
            f.write('content1')

        # Create a temporary backup directory
        with tempfile.TemporaryDirectory() as backup_dir:
            # Make the source folder read-only
            os.chmod(src_folder, 0o444)

            result = task_func(src_folder, backup_dir)

            # Check if the source folder still exists (due to the read-only attribute)
            assert os.path.exists(src_folder)

            # Check if the backup folder exists and contains the same files
            backup_folder = os.path.join(backup_dir, os.path.basename(src_folder))
            assert os.path.isdir(backup_folder)
            assert set(os.listdir(backup_folder)) == {'file1.txt'}
            with open(os.path.join(backup_folder, 'file1.txt'), 'r') as f:
                assert f.read() == 'content1'

            # Check if the function returned False
            assert result is False