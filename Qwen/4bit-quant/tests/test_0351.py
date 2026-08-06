import pytest
from src_0351 import task_func
import os
import tempfile

def test_task_func_success():
    with tempfile.TemporaryDirectory() as src_folder, tempfile.TemporaryDirectory() as dst_folder:
        # Create some files in the source directory
        with open(os.path.join(src_folder, 'file1.txt'), 'w') as f:
            f.write('content1')
        with open(os.path.join(src_folder, 'file2.txt'), 'w') as f:
            f.write('content2')

        result = task_func(src_folder, dst_folder)

        assert result['success'] is True
        assert result['message'] == 'All files compressed and moved successfully.'
        assert result['failed_files'] == []

        # Check if files are compressed and moved
        assert not os.path.exists(os.path.join(src_folder, 'file1.txt'))
        assert not os.path.exists(os.path.join(src_folder, 'file2.txt'))
        assert os.path.exists(os.path.join(dst_folder, 'file1.txt.gz'))
        assert os.path.exists(os.path.join(dst_folder, 'file2.txt.gz'))

def test_task_func_failure_compress():
    with tempfile.TemporaryDirectory() as src_folder, tempfile.TemporaryDirectory() as dst_folder:
        # Create a file that cannot be compressed (e.g., a non-existent file)
        with open(os.path.join(src_folder, 'file1.txt'), 'w') as f:
            f.write('content1')

        # Mock subprocess.Popen to simulate a compression failure
        def mock_popen(args):
            class MockProcess:
                def wait(self):
                    return 1
            return MockProcess()

        import subprocess
        subprocess.Popen = mock_popen

        result = task_func(src_folder, dst_folder)

        assert result['success'] is False
        assert result['message'] == 'Some files failed to compress or move.'
        assert result['failed_files'] == ['file1.txt']

def test_task_func_failure_move():
    with tempfile.TemporaryDirectory() as src_folder, tempfile.TemporaryDirectory() as dst_folder:
        # Create a compressed file
        with open(os.path.join(src_folder, 'file1.txt'), 'w') as f:
            f.write('content1')
        os.system(f'gzip {os.path.join(src_folder, "file1.txt")}')

        # Remove write permission from the destination folder to simulate a move failure
        os.chmod(dst_folder, 0o444)

        result = task_func(src_folder, dst_folder)

        assert result['success'] is False
        assert result['message'] == 'Some files failed to compress or move.'
        assert result['failed_files'] == ['file1.txt.gz']

        # Restore write permission
        os.chmod(dst_folder, 0o777)

def test_task_func_nonexistent_src():
    with tempfile.TemporaryDirectory() as dst_folder:
        src_folder = '/nonexistent/path'

        with pytest.raises(ValueError) as excinfo:
            task_func(src_folder, dst_folder)

        assert str(excinfo.value) == f"Source folder '{src_folder}' does not exist."

def test_task_func_nonexistent_dst():
    with tempfile.TemporaryDirectory() as src_folder:
        dst_folder = '/nonexistent/path'

        with pytest.raises(ValueError) as excinfo:
            task_func(src_folder, dst_folder)

        assert str(excinfo.value) == f"Destination folder '{dst_folder}' does not exist."