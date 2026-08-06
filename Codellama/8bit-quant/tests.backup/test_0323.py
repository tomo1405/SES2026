import pytest
from src_0323 import task_func

def test_task_func_valid_file():
    filename = 'test_file.txt'
    file_path = os.path.join(DIRECTORY, filename)
    backup_path = os.path.join(BACKUP_DIRECTORY, filename)

    # Create a temporary file
    with open(file_path, 'w') as f:
        f.write('test content')

    # Backup the file
    shutil.copy(file_path, backup_path)

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
    shutil.copy(file_path, backup_path)

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
    shutil.copy(file_path, backup_path)

    # Execute the file as a subprocess
    process = subprocess.Popen(file_path)
    exit_code = process.poll()

    # Check that the file was backed up and executed successfully
    assert os.path.exists(backup_path)
    assert exit_code == 0

def test_task_func_invalid_file_path():
    filename = 'test_file.txt'
    file_path = os.path.join(DIRECTORY, filename)
    backup_path = os.path.join(BACKUP_DIRECTORY, filename)

    # Create a temporary file
    with open(file_path, 'w') as f:
        f.write('test content')

    # Backup the file
    shutil.copy(file_path, backup_path)

    # Execute the file as a subprocess
    process = subprocess.Popen(file_path)
    exit_code = process.poll()

    # Check that the file was backed up and executed successfully
    assert os.path.exists(backup_path)
    assert exit_code == 0