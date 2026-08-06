python
import os
import shutil
import pytest

# Constants
BACKUP_DIR = '/tmp/backup'

def task_func(directory):
    # Check if the backup directory exists
    if not os.path.exists(BACKUP_DIR):
        return f'Backup directory {BACKUP_DIR} does not exist. Cannot rollback update.'

    backups = sorted(os.listdir(BACKUP_DIR))
    latest_backup = backups[-1] if backups else None

    if not latest_backup:
        return f'No backups found in {BACKUP_DIR}. Cannot rollback update.'

    if os.path.exists(directory):
        shutil.rmtree(directory)

    shutil.copytree(os.path.join(BACKUP_DIR, latest_backup), directory)
    return directory

def test_task_func():
    # Test case 1: Backup directory does not exist
    with pytest.raises(Exception) as e:
        task_func('/tmp/test')
    assert str(e.value) == 'Backup directory /tmp/backup does not exist. Cannot rollback update.'

    # Test case 2: No backups found
    with pytest.raises(Exception) as e:
        task_func('/tmp/test2')
    assert str(e.value) == 'No backups found in /tmp/backup. Cannot rollback update.'

    # Test case 3: Backup directory exists, but no backup found
    with pytest.raises(Exception) as e:
        task_func('/tmp/test3')
    assert str(e.value) == 'No backups found in /tmp/backup. Cannot rollback update.'

    # Test case 4: Backup directory exists, backup found, but directory already exists
    os.makedirs('/tmp/test4')
    with pytest.raises(Exception) as e:
        task_func('/tmp/test4')
    assert str(e.value) == 'Backup directory /tmp/backup/2021-01-01-00-00-00 already exists. Cannot rollback update.'

    # Test case 5: Backup directory exists, backup found, directory does not exist
    os.makedirs('/tmp/test5')
    os.makedirs('/tmp/backup/2021-01-01-00-00-00')
    assert task_func('/tmp/test5') == '/tmp/test5'

    # Test case 6: Backup directory exists, backup found, directory does not exist, but backup is empty
    os.makedirs('/tmp/test6')
    os.makedirs('/tmp/backup/2021-01-01-00-00-00')
    with open('/tmp/backup/2021-01-01-00-00-00/test6', 'w') as f:
        f.write('')
    with pytest.raises(Exception) as e:
        task_func('/tmp/test6')
    assert str(e.value) == 'Backup directory /tmp/backup/2021-01-01-00-00-00 is empty. Cannot rollback update.'

    # Test case 7: Backup directory exists, backup found, directory does not exist, backup is not empty
    os.makedirs('/tmp/test7')
    os.makedirs('/tmp/backup/2021-01-01-00-00-00')
    with open('/tmp/backup/2021-01-01-00-00-00/test7', 'w') as f:
        f.write('test')
    assert task_func('/tmp/test7') == '/tmp/test7'