import pytest
from src_0323 import task_func

def test_task_func():
    # Test case 1: file exists and can be backed up
    filename = 'test_file.txt'
    file_path = os.path.join(DIRECTORY, filename)
    backup_path = os.path.join(BACKUP_DIRECTORY, filename)
    with open(file_path, 'w') as f:
        f.write('test data')
    assert task_func(filename) == 0
    assert os.path.exists(backup_path)
    os.remove(backup_path)

    # Test case 2: file does not exist
    filename = 'test_file_2.txt'
    file_path = os.path.join(DIRECTORY, filename)
    backup_path = os.path.join(BACKUP_DIRECTORY, filename)
    assert task_func(filename) == -1
    assert not os.path.exists(backup_path)

    # Test case 3: file cannot be backed up
    filename = 'test_file_3.txt'
    file_path = os.path.join(DIRECTORY, filename)
    backup_path = os.path.join(BACKUP_DIRECTORY, filename)
    with open(file_path, 'w') as f:
        f.write('test data')
    os.chmod(backup_path, 0o000)
    assert task_func(filename) == -1
    assert not os.path.exists(backup_path)

    # Test case 4: file cannot be executed
    filename = 'test_file_4.txt'
    file_path = os.path.join(DIRECTORY, filename)
    backup_path = os.path.join(BACKUP_DIRECTORY, filename)
    with open(file_path, 'w') as f:
        f.write('test data')
    os.chmod(file_path, 0o000)
    assert task_func(filename) == -1
    assert not os.path.exists(backup_path)