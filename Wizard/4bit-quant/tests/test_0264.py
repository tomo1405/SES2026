python
import os
import glob
import shutil
import time
import pytest

# Constants
FILE_EXTENSIONS = ['.txt', '.csv', '.xlsx', '.docx', '.pdf']

def task_func(my_path: str, days_old: int) -> str:

    archive_dir = os.path.join(my_path, 'archive')
    os.makedirs(archive_dir, exist_ok=True)

    for ext in FILE_EXTENSIONS:
        files = glob.glob(os.path.join(my_path, '*' + ext))
        for file in files:
            if os.path.isfile(file) and os.path.getmtime(file) < time.time() - days_old * 86400:
                shutil.move(file, archive_dir)

    return archive_dir

def test_task_func():
    # Test case 1: Archive files older than 30 days
    my_path = '/path/to/files'
    days_old = 30
    expected_archive_dir = os.path.join(my_path, 'archive')
    expected_files = ['file1.txt', 'file2.csv', 'file3.xlsx', 'file4.docx', 'file5.pdf']
    # Create files in the directory
    for file in expected_files:
        with open(os.path.join(my_path, file), 'w') as f:
            f.write('test')
    # Set modification time of files to 30 days ago
    for file in expected_files:
        os.utime(os.path.join(my_path, file), (time.time() - 30 * 86400, time.time() - 30 * 86400))
    # Call the function
    archive_dir = task_func(my_path, days_old)
    # Check if the archive directory was created
    assert os.path.exists(expected_archive_dir)
    # Check if the files were moved to the archive directory
    for file in expected_files:
        assert not os.path.exists(os.path.join(my_path, file))
        assert os.path.exists(os.path.join(expected_archive_dir, file))
    # Test case 2: Archive files older than 7 days
    my_path = '/path/to/files'
    days_old = 7
    expected_archive_dir = os.path.join(my_path, 'archive')
    expected_files = ['file1.txt', 'file2.csv', 'file3.xlsx', 'file4.docx', 'file5.pdf']
    # Create files in the directory
    for file in expected_files:
        with open(os.path.join(my_path, file), 'w') as f:
            f.write('test')
    # Set modification time of files to 7 days ago
    for file in expected_files:
        os.utime(os.path.join(my_path, file), (time.time() - 7 * 86400, time.time() - 7 * 86400))
    # Call the function
    archive_dir = task_func(my_path, days_old)
    # Check if the archive directory was created
    assert os.path.exists(expected_archive_dir)
    # Check if the files were moved to the archive directory
    for file in expected_files:
        assert not os.path.exists(os.path.join(my_path, file))
        assert os.path.exists(os.path.join(expected_archive_dir, file))
    # Test case 3: Archive files older than 0 days
    my_path = '/path/to/files'
    days_old = 0
    expected_archive_dir = os.path.join(my_path, 'archive')
    expected_files = ['file1.txt', 'file2.csv', 'file3.xlsx', 'file4.docx', 'file5.pdf']
    # Create files in the directory
    for file in expected_files:
        with open(os.path.join(my_path, file), 'w') as f:
            f.write('test')
    # Set modification time of files to 0 days ago
    for file in expected_files:
        os.utime(os.path.join(my_path, file), (time.time() - 0 * 86400, time.time() - 0 * 86400))
    # Call the function
    archive_dir = task_func(my_path, days_old)
    # Check if the archive directory was created
    assert os.path.exists(expected_archive_dir)
    # Check if the files were moved to the archive directory
    for file in expected_files:
        assert not os.path.exists(os.path.join(my_path, file))
        assert os.path.exists(os.path.join(expected_archive_dir, file))
    # Test case 4: Archive files older than 365 days
    my_path = '/path/to/files'
    days_old = 365
    expected_archive_dir = os.path.join(my_path, 'archive')
    expected_files = ['file1.txt', 'file2.csv', 'file3.xlsx', 'file4.docx', 'file5.pdf']
    # Create files in the directory
    for file in expected_files:
        with open(os.path.join(my_path, file), 'w') as f:
            f.write('test')
    # Set modification time of files to 365 days ago
    for file in expected_files:
        os.utime(os.path.join(my_path, file), (time.time() - 365 * 86400, time.time() - 365 * 86400))
    # Call the function
    archive_dir = task_func(my_path, days_old)
    # Check if the archive directory was created
    assert os.path.exists(expected_archive_dir)
    # Check if the files were moved to the archive directory
    for file in expected_files:
        assert not os.path.exists(os.path.join(my_path, file))
        assert os.path.exists(os.path.join(expected_archive_dir, file))