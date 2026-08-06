from src_0799 import task_func

BACKUP_DIR = '/tmp/backup'

def test_task_func_with_existing_backup_dir():
    # Mock the os.path.exists function to return True for the backup directory
    with mock.patch('os.path.exists') as mock_exists:
        mock_exists.return_value = True

        # Call the function and assert the expected output
        result = task_func('/path/to/directory')
        assert result == '/path/to/directory'

def test_task_func_with_no_backup_dir():
    # Mock the os.path.exists function to return False for the backup directory
    with mock.patch('os.path.exists') as mock_exists:
        mock_exists.return_value = False

        # Call the function and assert the expected output
        result = task_func('/path/to/directory')
        assert result == f'Backup directory {BACKUP_DIR} does not exist. Cannot rollback update.'

def test_task_func_with_no_backups():
    # Mock the os.path.exists function to return True for the backup directory
    with mock.patch('os.path.exists') as mock_exists:
        mock_exists.return_value = True

    # Mock the os.listdir function to return an empty list
    with mock.patch('os.listdir') as mock_listdir:
        mock_listdir.return_value = []

        # Call the function and assert the expected output
        result = task_func('/path/to/directory')
        assert result == f'No backups found in {BACKUP_DIR}. Cannot rollback update.'

def test_task_func_with_existing_directory():
    # Mock the os.path.exists function to return True for the backup directory
    with mock.patch('os.path.exists') as mock_exists:
        mock_exists.return_value = True

    # Mock the shutil.rmtree function to raise an OSError
    with mock.patch('shutil.rmtree') as mock_rmtree:
        mock_rmtree.side_effect = OSError()

        # Call the function and assert the expected output
        result = task_func('/path/to/directory')
        assert result == f'Failed to remove existing directory /path/to/directory. Cannot rollback update.'

def test_task_func_with_copytree_error():
    # Mock the os.path.exists function to return True for the backup directory
    with mock.patch('os.path.exists') as mock_exists:
        mock_exists.return_value = True

    # Mock the os.listdir function to return a list with a single backup
    with mock.patch('os.listdir') as mock_listdir:
        mock_listdir.return_value = ['backup_20230101']

    # Mock the shutil.copytree function to raise an OSError
    with mock.patch('shutil.copytree') as mock_copytree:
        mock_copytree.side_effect = OSError()

        # Call the function and assert the expected output
        result = task_func('/path/to/directory')
        assert result == f'Failed to copy backup backup_20230101 to /path/to/directory. Cannot rollback update.'