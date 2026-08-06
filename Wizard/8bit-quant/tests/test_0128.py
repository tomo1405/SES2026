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
    ROOT_DIR = 'test_dir'
    DEST_DIR = 'dest_dir'
    SPECIFIC_HASH = 'specific_hash'

    os.makedirs(ROOT_DIR, exist_ok=True)
    with open(os.path.join(ROOT_DIR, 'file1.txt'), 'w') as f:
        f.write('content1')
    with open(os.path.join(ROOT_DIR, 'file2.txt'), 'w') as f:
        f.write('content2')
    with open(os.path.join(ROOT_DIR, 'file3.txt'), 'w') as f:
        f.write('content3')

    # Test with valid hash
    with open(os.path.join(ROOT_DIR, 'file1.txt'), 'rb') as f:
        file_hash = hashlib.md5(f.read()).hexdigest()
    assert file_hash == 'd41d8cd98f00b204e9800998ecf8427e'

    # Test with invalid hash
    with open(os.path.join(ROOT_DIR, 'file2.txt'), 'rb') as f:
        file_hash = hashlib.md5(f.read()).hexdigest()
    assert file_hash != 'specific_hash'

    # Test with file not found
    with pytest.raises(FileNotFoundError):
        task_func(ROOT_DIR, DEST_DIR, 'invalid_hash')

    # Test with file moved
    task_func(ROOT_DIR, DEST_DIR, SPECIFIC_HASH)
    assert os.path.exists(os.path.join(DEST_DIR, 'file1.txt'))
    assert not os.path.exists(os.path.join(ROOT_DIR, 'file1.txt'))
    assert os.path.exists(os.path.join(DEST_DIR, 'file2.txt'))
    assert not os.path.exists(os.path.join(ROOT_DIR, 'file2.txt'))
    assert not os.path.exists(os.path.join(DEST_DIR, 'file3.txt'))
    assert os.path.exists(os.path.join(ROOT_DIR, 'file3.txt'))

    # Test with empty directory
    os.makedirs(os.path.join(ROOT_DIR, 'empty_dir'), exist_ok=True)
    task_func(ROOT_DIR, DEST_DIR, SPECIFIC_HASH)
    assert os.path.exists(os.path.join(DEST_DIR, 'empty_dir'))
    assert not os.path.exists(os.path.join(ROOT_DIR, 'empty_dir'))

    # Test with directory
    os.makedirs(os.path.join(ROOT_DIR, 'dir'), exist_ok=True)
    with open(os.path.join(ROOT_DIR, 'dir', 'file4.txt'), 'w') as f:
        f.write('content4')
    task_func(ROOT_DIR, DEST_DIR, SPECIFIC_HASH)
    assert os.path.exists(os.path.join(DEST_DIR, 'dir'))
    assert not os.path.exists(os.path.join(ROOT_DIR, 'dir'))
    assert os.path.exists(os.path.join(DEST_DIR, 'dir', 'file4.txt'))
    assert not os.path.exists(os.path.join(ROOT_DIR, 'dir', 'file4.txt'))

    # Test with non-existent directory
    with pytest.raises(NotADirectoryError):
        task_func('non_existent_dir', DEST_DIR, SPECIFIC_HASH)

    # Test with non-existent destination directory
    with pytest.raises(NotADirectoryError):
        task_func(ROOT_DIR, 'non_existent_dest_dir', SPECIFIC_HASH)

    # Test with empty root directory
    os.rmdir(ROOT_DIR)
    with pytest.raises(FileNotFoundError):
        task_func(ROOT_DIR, DEST_DIR, SPECIFIC_HASH)

    # Test with empty destination directory
    os.makedirs(DEST_DIR, exist_ok=True)
    task_func(ROOT_DIR, DEST_DIR, SPECIFIC_HASH)
    assert not os.path.exists(os.path.join(DEST_DIR, 'file1.txt'))
    assert not os.path.exists(os.path.join(DEST_DIR, 'file2.txt'))
    assert not os.path.exists(os.path.join(DEST_DIR, 'file3.txt'))
    assert not os.path.exists(os.path.join(DEST_DIR, 'empty_dir'))
    assert not os.path.exists(os.path.join(DEST_DIR, 'dir'))

    # Test with empty root and destination directory
    os.makedirs(ROOT_DIR, exist_ok=True)
    os.makedirs(DEST_DIR, exist_ok=True)
    task_func(ROOT_DIR, DEST_DIR, SPECIFIC_HASH)
    assert not os.path.exists(os.path.join(DEST_DIR, 'file1.txt'))
    assert not os.path.exists(os.path.join(DEST_DIR, 'file2.txt'))
    assert not os.path.exists(os.path.join(DEST_DIR, 'file3.txt'))
    assert not os.path.exists(os.path.join(DEST_DIR, 'empty_dir'))
    assert not os.path.exists(os.path.join(DEST_DIR, 'dir'))