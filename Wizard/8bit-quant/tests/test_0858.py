python
import pytest
from src_0858 import task_func

def test_task_func():
    SOURCE_DIR = 'source_dir'
    DEST_DIR = 'dest_dir'
    EXTENSIONS = ['.txt', '.pdf']

    # Test with valid input
    os.makedirs(SOURCE_DIR, exist_ok=True)
    os.makedirs(DEST_DIR, exist_ok=True)
    with open(os.path.join(SOURCE_DIR, 'file1.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(SOURCE_DIR, 'file2.pdf'), 'w') as f:
        f.write('test')
    transferred_files = task_func(SOURCE_DIR, DEST_DIR, EXTENSIONS)
    assert transferred_files == ['file1.txt', 'file2.pdf']
    assert os.path.exists(os.path.join(DEST_DIR, 'file1.txt'))
    assert os.path.exists(os.path.join(DEST_DIR, 'file2.pdf'))

    # Test with invalid input
    with pytest.raises(Exception):
        task_func('invalid_source_dir', DEST_DIR, EXTENSIONS)
    with pytest.raises(Exception):
        task_func(SOURCE_DIR, 'invalid_dest_dir', EXTENSIONS)
    with pytest.raises(Exception):
        task_func(SOURCE_DIR, DEST_DIR, ['.invalid_extension'])
    with pytest.raises(Exception):
        task_func(SOURCE_DIR, DEST_DIR, ['.txt', '.invalid_extension'])
    with pytest.raises(Exception):
        task_func(SOURCE_DIR, DEST_DIR, ['.txt', '.pdf', '.invalid_extension'])