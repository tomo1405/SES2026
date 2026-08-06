import os
import shutil
import subprocess
import sys


def test_task_func_valid_file():
    filename = 'test_file.txt'
    file_path = os.path.join(DIRECTORY, filename)
    backup_path = os.path.join(BACKUP_DIRECTORY, filename)

    # Create a temporary file
    with open(file_path, 'w') as f:
        f.write('test content')

    # Backup the file
    try:
        shutil.copy(file_path, backup_path)
    except Exception as e:
        print(f"Failed to backup the file: {e}", file=sys.stderr)
        return -1

    # Execute the file as a subprocess
    process = subprocess.Popen(file_path)
    exit_code = process.poll()

    # Check that the file was backed up and executed successfully
    assert os.path.exists(backup_path)
    assert exit_code == 0

def test_task_func_invalid_file():
    filename = 'invalid_file.txt'
    file_path = os.path.join(DIRECTORY, filename)
    backup_path = os.path.join(BACKUP_DIRECTORY, filename)

    # Create a temporary file
    with open(file_path, 'w') as f:
        f.write('test content')

    # Backup the file
    try:
        shutil.copy(file_path, backup_path)
    except Exception as e:
        print(f"Failed to backup the file: {e}", file=sys.stderr)
        return -1

    # Execute the file as a subprocess
    process = subprocess.Popen(file_path)
    exit_code = process.poll()

    # Check that the file was backed up and executed successfully
    assert os.path.exists(backup_path)
    assert exit_code == 0

def test_task_func_invalid_directory():
    filename = 'test_file.txt'
    file_path = os.path.join(DIRECTORY, filename)
    backup_path = os.path.join(BACKUP_DIRECTORY, filename)

    # Create a temporary file
    with open(file_path, 'w') as f:
        f.write('test content')

    # Backup the file
    try:
        shutil.copy(file_path, backup_path)
    except Exception as e:
        print(f"Failed to backup the file: {e}", file=sys.stderr)
        return -1

    # Execute the file as a subprocess
    process = subprocess.Popen(file_path)
    exit_code = process.poll()

    # Check that the file was backed up and executed successfully
    assert os.path.exists(backup_path)
    assert exit_code == 0