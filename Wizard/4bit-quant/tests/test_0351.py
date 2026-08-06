python
import subprocess
import os
import shutil
from glob import glob

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
    result = task_func('/tmp/src', '/tmp/dst')
    assert result['success'] == True
    assert result['message'] == 'All files compressed and moved successfully.'
    assert result['failed_files'] == []

    # Test with invalid input
    try:
        task_func('/tmp/invalid_src', '/tmp/dst')
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Source folder '/tmp/invalid_src' does not exist."

    try:
        task_func('/tmp/src', '/tmp/invalid_dst')
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Destination folder '/tmp/invalid_dst' does not exist."

    # Test with failing processes
    def mock_subprocess_Popen(args, **kwargs):
        if args[0] == 'gzip':
            return MockPopen(returncode=1)
        else:
            return MockPopen()

    class MockPopen:
        def __init__(self, returncode=0):
            self.returncode = returncode

        def wait(self):
            return self.returncode

    subprocess.Popen = mock_subprocess_Popen

    result = task_func('/tmp/src', '/tmp/dst')
    assert result['success'] == False
    assert result['message'] == 'Some files failed to compress or move.'
    assert result['failed_files'] == ['file1.txt', 'file2.txt']

    # Test with failing moves
    def mock_shutil_move(src, dst):
        raise Exception("Failed to move file")

    shutil.move = mock_shutil_move

    result = task_func('/tmp/src', '/tmp/dst')
    assert result['success'] == False
    assert result['message'] == 'Some files failed to compress or move.'
    assert result['failed_files'] == ['file1.txt', 'file2.txt', 'file3.txt']