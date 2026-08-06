python
import os
import shutil
import glob
import hashlib
import pytest

def task_func(ROOT_DIR, DEST_DIR, SPECIFIC_HASH):
    files_moved = 0

    os.makedirs(DEST_DIR, exist_ok=True)
    for filename in glob.glob(os.path.join(ROOT_DIR, '*')):
        if not os.path.exists(filename) or os.path.isdir(filename):
            continue
        with open(filename, 'rb') as f:
            file_hash = hashlib.md5(f.read()).hexdigest()
        if file_hash == SPECIFIC_HASH:
            shutil.move(filename, DEST_DIR)
            files_moved += 1
    return files_moved

def test_task_func():
    ROOT_DIR = 'tests/data'
    DEST_DIR = 'tests/dest'
    SPECIFIC_HASH = '1234567890abcdef1234567890abcdef'

    # Test case 1: Move a file with the specified hash
    os.makedirs(ROOT_DIR, exist_ok=True)
    with open(os.path.join(ROOT_DIR, 'test_file.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(ROOT_DIR, 'test_file.txt'), 'rb') as f:
        file_hash = hashlib.md5(f.read()).hexdigest()
    assert file_hash == 'e8dc44f8d15a1e2d9d5c8d5d9e1b9c8a'
    shutil.move(os.path.join(ROOT_DIR, 'test_file.txt'), DEST_DIR)

    files_moved = task_func(ROOT_DIR, DEST_DIR, SPECIFIC_HASH)
    assert files_moved == 1
    assert os.path.exists(os.path.join(DEST_DIR, 'test_file.txt'))

    # Test case 2: Do not move a file with a different hash
    with open(os.path.join(ROOT_DIR, 'test_file2.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(ROOT_DIR, 'test_file2.txt'), 'rb') as f:
        file_hash = hashlib.md5(f.read()).hexdigest()
    assert file_hash == 'e8dc44f8d15a1e2d9d5c8d5d9e1b9c8a'
    files_moved = task_func(ROOT_DIR, DEST_DIR, SPECIFIC_HASH)
    assert files_moved == 1
    assert os.path.exists(os.path.join(DEST_DIR, 'test_file2.txt'))

    # Test case 3: Do not move a file that does not exist
    files_moved = task_func(ROOT_DIR, DEST_DIR, '0123456789abcdef0123456789abcdef')
    assert files_moved == 0
    assert not os.path.exists(os.path.join(DEST_DIR, 'test_file2.txt'))

    # Test case 4: Do not move a file that is a directory
    os.makedirs(os.path.join(ROOT_DIR, 'test_dir'), exist_ok=True)
    files_moved = task_func(ROOT_DIR, DEST_DIR, SPECIFIC_HASH)
    assert files_moved == 1
    assert os.path.exists(os.path.join(DEST_DIR, 'test_dir'))

    # Test case 5: Move multiple files with the specified hash
    os.makedirs(os.path.join(ROOT_DIR, 'test_dir2'), exist_ok=True)
    with open(os.path.join(ROOT_DIR, 'test_file3.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(ROOT_DIR, 'test_file4.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(ROOT_DIR, 'test_file3.txt'), 'rb') as f:
        file_hash = hashlib.md5(f.read()).hexdigest()
    assert file_hash == 'e8dc44f8d15a1e2d9d5c8d5d9e1b9c8a'
    with open(os.path.join(ROOT_DIR, 'test_file4.txt'), 'rb') as f:
        file_hash = hashlib.md5(f.read()).hexdigest()
    assert file_hash == 'e8dc44f8d15a1e2d9d5c8d5d9e1b9c8a'
    shutil.move(os.path.join(ROOT_DIR, 'test_file3.txt'), DEST_DIR)
    shutil.move(os.path.join(ROOT_DIR, 'test_file4.txt'), DEST_DIR)

    files_moved = task_func(ROOT_DIR, DEST_DIR, SPECIFIC_HASH)
    assert files_moved == 2
    assert os.path.exists(os.path.join(DEST_DIR, 'test_file3.txt'))
    assert os.path.exists(os.path.join(DEST_DIR, 'test_file4.txt'))

    # Test case 6: Do not move a file that has already been moved
    files_moved = task_func(ROOT_DIR, DEST_DIR, SPECIFIC_HASH)
    assert files_moved == 0
    assert os.path.exists(os.path.join(DEST_DIR, 'test_file3.txt'))
    assert os.path.exists(os.path.join(DEST_DIR, 'test_file4.txt'))

    # Test case 7: Move a file with a different hash but with a different filename
    with open(os.path.join(ROOT_DIR, 'test_file5.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(ROOT_DIR, 'test_file5.txt'), 'rb') as f:
        file_hash = hashlib.md5(f.read()).hexdigest()
    assert file_hash == 'e8dc44f8d15a1e2d9d5c8d5d9e1b9c8a'
    shutil.move(os.path.join(ROOT_DIR, 'test_file5.txt'), DEST_DIR)

    files_moved = task_func(ROOT_DIR, DEST_DIR, '0123456789abcdef0123456789abcdef')
    assert files_moved == 1
    assert os.path.exists(os.path.join(DEST_DIR, 'test_file5.txt'))

    # Test case 8: Move a file with a different hash but with a different filename
    with open(os.path.join(ROOT_DIR, 'test_file6.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(ROOT_DIR, 'test_file6.txt'), 'rb') as f:
        file_hash = hashlib.md5(f.read()).hexdigest()
    assert file_hash == 'e8dc44f8d15a1e2d9d5c8d5d9e1b9c8a'
    shutil.move(os.path.join(ROOT_DIR, 'test_file6.txt'), DEST_DIR)

    files_moved = task_func(ROOT_DIR, DEST_DIR, '0123456789abcdef0123456789abcdef')
    assert files_moved == 1
    assert os.path.exists(os.path.join(DEST_DIR, 'test_file6.txt'))