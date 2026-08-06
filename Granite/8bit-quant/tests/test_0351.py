import subprocess
import os
import shutil
from glob import glob
from unittest.mock import patch, call

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
    with patch('subprocess.Popen') as mock_popen, patch('os.path.isdir') as mock_isdir, patch('shutil.move') as mock_move:
        mock_isdir.return_value = True
        task_func('/path/to/src', '/path/to/dst')
        mock_popen.assert_has_calls([
            call(['gzip', '/path/to/src/file1']),
            call().wait(),
            call(['gzip', '/path/to/src/file2']),
            call().wait(),
            call(['gzip', '/path/to/src/file3']),
            call().wait()
        ])
        mock_move.assert_has_calls([
            call('/path/to/src/file1.gz', '/path/to/dst'),
            call('/path/to/src/file2.gz', '/path/to/dst'),
            call('/path/to/src/file3.gz', '/path/to/dst')
        ])