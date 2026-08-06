python
import pytest
from src_0907 import task_func

def test_task_func():
    # Test case 1: source_dir does not exist
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent_dir', 'target_dir')
        
    # Test case 2: target_dir does not exist
    with pytest.raises(FileNotFoundError):
        task_func('source_dir', 'nonexistent_dir')
        
    # Test case 3: source_dir is empty
    with pytest.raises(ValueError):
        task_func('empty_dir', 'target_dir')
        
    # Test case 4: source_dir contains only processed files
    source_dir = 'source_dir'
    target_dir = 'target_dir'
    os.makedirs(source_dir, exist_ok=True)
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(source_dir, 'file_processed.txt'), 'w') as f:
        f.write('processed')
    with open(os.path.join(source_dir, 'file_not_processed.txt'), 'w') as f:
        f.write('not processed')
    with pytest.raises(ValueError):
        task_func(source_dir, target_dir)
        
    # Test case 5: source_dir contains only unprocessed files
    source_dir = 'source_dir'
    target_dir = 'target_dir'
    os.makedirs(source_dir, exist_ok=True)
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(source_dir, 'file_not_processed.txt'), 'w') as f:
        f.write('not processed')
    with open(os.path.join(source_dir, 'file_not_processed2.txt'), 'w') as f:
        f.write('not processed')
    archive_path = task_func(source_dir, target_dir)
    assert os.path.exists(archive_path)
    assert os.path.isfile(archive_path)
    assert os.path.getsize(archive_path) > 0
    os.remove(archive_path)
        
    # Test case 6: source_dir contains both processed and unprocessed files
    source_dir = 'source_dir'
    target_dir = 'target_dir'
    os.makedirs(source_dir, exist_ok=True)
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(source_dir, 'file_processed.txt'), 'w') as f:
        f.write('processed')
    with open(os.path.join(source_dir, 'file_not_processed.txt'), 'w') as f:
        f.write('not processed')
    with open(os.path.join(source_dir, 'file_not_processed2.txt'), 'w') as f:
        f.write('not processed')
    archive_path = task_func(source_dir, target_dir)
    assert os.path.exists(archive_path)
    assert os.path.isfile(archive_path)
    assert os.path.getsize(archive_path) > 0
    os.remove(archive_path)