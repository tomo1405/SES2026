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
    ROOT_DIR = 'path/to/root/dir'
    DEST_DIR = 'path/to/dest/dir'
    SPECIFIC_HASH = '1234567890abcdef1234567890abcdef'
    files_moved = task_func(ROOT_DIR, DEST_DIR, SPECIFIC_HASH)
    assert files_moved > 0, "No files were moved"

if __name__ == "__main__":
    pytest.main()