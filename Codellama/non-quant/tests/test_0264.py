import os

from src_0264 import task_func


def test_task_func():
    # Test case 1: No files to move
    my_path = 'path/to/files'
    days_old = 10
    archive_dir = task_func(my_path, days_old)
    assert archive_dir == os.path.join(my_path, 'archive')
    assert not os.path.exists(archive_dir)

    # Test case 2: Some files to move
    my_path = 'path/to/files'
    days_old = 10
    for ext in FILE_EXTENSIONS:
        file = os.path.join(my_path, 'file' + ext)
        with open(file, 'w') as f:
            f.write('test')
    archive_dir = task_func(my_path, days_old)
    assert archive_dir == os.path.join(my_path, 'archive')
    assert os.path.exists(archive_dir)
    for ext in FILE_EXTENSIONS:
        file = os.path.join(archive_dir, 'file' + ext)
        assert os.path.exists(file)

    # Test case 3: No files to move, but archive directory exists
    my_path = 'path/to/files'
    days_old = 10
    archive_dir = os.path.join(my_path, 'archive')
    os.makedirs(archive_dir, exist_ok=True)
    archive_dir = task_func(my_path, days_old)
    assert archive_dir == os.path.join(my_path, 'archive')
    assert os.path.exists(archive_dir)

    # Test case 4: Some files to move, but archive directory exists
    my_path = 'path/to/files'
    days_old = 10
    for ext in FILE_EXTENSIONS:
        file = os.path.join(my_path, 'file' + ext)
        with open(file, 'w') as f:
            f.write('test')
    archive_dir = os.path.join(my_path, 'archive')
    os.makedirs(archive_dir, exist_ok=True)
    archive_dir = task_func(my_path, days_old)
    assert archive_dir == os.path.join(my_path, 'archive')
    assert os.path.exists(archive_dir)
    for ext in FILE_EXTENSIONS:
        file = os.path.join(archive_dir, 'file' + ext)
        assert os.path.exists(file)