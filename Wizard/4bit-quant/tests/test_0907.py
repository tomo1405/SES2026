python
import pytest
from src_0907 import task_func

def test_task_func():
    # Test case 1: source_dir does not exist
    with pytest.raises(FileNotFoundError):
        task_func('non_existent_dir', 'target_dir')
        
    # Test case 2: target_dir does not exist
    with pytest.raises(FileNotFoundError):
        task_func('source_dir', 'non_existent_dir')
        
    # Test case 3: source_dir is empty
    with pytest.raises(ValueError):
        task_func('empty_dir', 'target_dir')
        
    # Test case 4: source_dir contains only processed files
    source_dir = 'source_dir'
    target_dir = 'target_dir'
    os.makedirs(source_dir, exist_ok=True)
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(source_dir, 'file1_processed'), 'w') as f:
        f.write('processed file')
    with open(os.path.join(source_dir, 'file2_processed'), 'w') as f:
        f.write('processed file')
    archive_path = task_func(source_dir, target_dir)
    assert os.path.exists(archive_path)
    assert os.path.isfile(archive_path)
    assert os.path.getsize(archive_path) > 0
    assert os.path.join(target_dir, 'file1_processed') in os.listdir(target_dir)
    assert os.path.join(target_dir, 'file2_processed') in os.listdir(target_dir)
    os.remove(archive_path)
    os.rmdir(target_dir)
    os.rmdir(source_dir)
    
    # Test case 5: source_dir contains files to be archived
    source_dir = 'source_dir'
    target_dir = 'target_dir'
    os.makedirs(source_dir, exist_ok=True)
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(source_dir, 'file1'), 'w') as f:
        f.write('unprocessed file')
    with open(os.path.join(source_dir, 'file2'), 'w') as f:
        f.write('unprocessed file')
    archive_path = task_func(source_dir, target_dir)
    assert os.path.exists(archive_path)
    assert os.path.isfile(archive_path)
    assert os.path.getsize(archive_path) > 0
    assert os.path.join(target_dir, 'file1') in os.listdir(target_dir)
    assert os.path.join(target_dir, 'file2') in os.listdir(target_dir)
    os.remove(archive_path)
    os.rmdir(target_dir)
    os.rmdir(source_dir)