python
import subprocess
import os
import shutil
from glob import glob
import pytest

def task_func(src_folder, dst_folder):
    # Check if source and destination folders exist
    if not os.path.isdir(src_folder):
        raise ValueError(f"Source folder '{src_folder}' does not exist.")
    if not os.path.isdir(dst_folder):
        raise ValueError(f"Destination folder '{dst_folder}' does not exist.")
    
    processes = []
    failed_files = []

    # Compress files in a background process
    for file in glob(os.path.join(src_folder, '*')):
        process = subprocess.Popen(['gzip', file])
        processes.append((process, file))

    # Wait for all processes to complete
    for process, file in processes:
        retcode = process.wait()
        if retcode != 0:
            failed_files.append(os.path.basename(file))

    # Move compressed files to destination folder
    for file in glob(os.path.join(src_folder, '*.gz')):
        try:
            shutil.move(file, dst_folder)
        except Exception as e:
            failed_files.append(os.path.basename(file))

    if failed_files:
        return {'success': False, 'message': 'Some files failed to compress or move.', 'failed_files': failed_files}
    else:
        return {'success': True, 'message': 'All files compressed and moved successfully.', 'failed_files': []}

def test_task_func():
    # Test with valid input
    assert task_func('/tmp/src', '/tmp/dst') == {'success': True, 'message': 'All files compressed and moved successfully.', 'failed_files': []}

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func('/tmp/invalid_src', '/tmp/dst')

    # Test with failing processes
    def mock_subprocess_Popen(cmd, *args, **kwargs):
        if cmd[0] == 'gzip':
            return MockPopen(1)
        else:
            return MockPopen(0)

    class MockPopen:
        def __init__(self, retcode):
            self.retcode = retcode

        def wait(self):
            return self.retcode

    with pytest.raises(Exception):
        with mock.patch('subprocess.Popen', side_effect=mock_subprocess_Popen):
            task_func('/tmp/src', '/tmp/dst')

    # Test with failing file moves
    def mock_shutil_move(src, dst):
        if src.endswith('.gz'):
            raise Exception('Failed to move file')

    with pytest.raises(Exception):
        with mock.patch('shutil.move', side_effect=mock_shutil_move):
            task_func('/tmp/src', '/tmp/dst')