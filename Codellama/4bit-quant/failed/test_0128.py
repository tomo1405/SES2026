import pytest
from src_0128 import task_func

def test_task_func():
    ROOT_DIR = 'tests/test_data'
    DEST_DIR = 'tests/test_data/dest'
    SPECIFIC_HASH = '00000000000000000000000000000000'

    files_moved = task_func(ROOT_DIR, DEST_DIR, SPECIFIC_HASH)

    assert files_moved == 0

    for filename in glob.glob(os.path.join(ROOT_DIR, '*')):
        if not os.path.exists(filename) or os.path.isdir(filename):
            continue
        with open(filename, 'rb') as f:
            file_hash = hashlib.md5(f.read()).hexdigest()
        assert file_hash != SPECIFIC_HASH

    assert not os.path.exists(DEST_DIR)