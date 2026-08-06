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
    src_folder = 'source_folder'
    dst_folder = 'destination_folder'
    result = task_func(src_folder, dst_folder)
    assert result['success'] == True
    assert result['message'] == 'All files compressed and moved successfully.'
    assert result['failed_files'] == []

def test_task_func_with_failed_files():
    src_folder = 'source_folder'
    dst_folder = 'destination_folder'
    # Create a test file that will fail to compress
    with open('test_file.txt', 'w') as f:
        f.write('Test file content')
    result = task_func(src_folder, dst_folder)
    assert result['success'] == False
    assert result['message'] == 'Some files failed to compress or move.'
    assert len(result['failed_files']) == 1
    assert result['failed_files'][0] == 'test_file.txt.gz'