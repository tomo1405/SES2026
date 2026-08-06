python
import os
import glob
import shutil
import pytest

def task_func(directory, archive_dir='archive'):
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    json_files = glob.glob(os.path.join(directory, '*.json'))
    error_messages = []

    for json_file in json_files:
        try:
            shutil.move(json_file, archive_dir)
        except Exception as e:
            error_message = f'Unable to move {json_file} due to {str(e)}'
            error_messages.append(error_message)

    return (len(error_messages) == 0, error_messages)

def test_task_func():
    # Test case 1: directory does not exist
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent_directory')

    # Test case 2: directory is empty
    assert task_func('tests/test_data/empty_directory') == (True, [])

    # Test case 3: directory contains JSON files
    assert task_func('tests/test_data/json_files') == (True, [])

    # Test case 4: directory contains JSON files and some errors
    assert task_func('tests/test_data/json_files_with_errors') == (False, ['Unable to move tests/test_data/json_files_with_errors/file1.json due to [Errno 2] No such file or directory: '])

    # Test case 5: directory contains JSON files and some errors, with custom archive directory
    assert task_func('tests/test_data/json_files_with_errors', 'custom_archive_dir') == (False, ['Unable to move tests/test_data/json_files_with_errors/file1.json due to [Errno 2] No such file or directory: '])