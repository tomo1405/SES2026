import pytest
from src_0815 import task_func

def test_task_func_basic():
    # Test basic functionality
    source_dir = 'test_source'
    target_dir = 'test_target'
    os.makedirs(source_dir)
    os.makedirs(target_dir)

    # Create a sample file in the source directory
    with open(os.path.join(source_dir, 'test_file.txt'), 'w') as f:
        f.write('test')

    result = task_func(source_dir, target_dir)

    assert result == 1
    assert os.path.exists(os.path.join(target_dir, 'test_file.txt'))

    # Clean up
    shutil.rmtree(source_dir)
    shutil.rmtree(target_dir)

def test_task_func_no_files():
    source_dir = 'test_source'
    target_dir = 'test_target'
    os.makedirs(source_dir)
    os.makedirs(target_dir)

    result = task_func(source_dir, target_dir)

    assert result == 0

    # Clean up
    shutil.rmtree(source_dir)
    shutil.rmtree(target_dir)

def test_task_func_invalid_source_dir():
    with pytest.raises(FileNotFoundError):
        task_func('invalid_source_dir', 'target_dir')

def test_task_func_invalid_target_dir():
    with pytest.raises(FileNotFoundError):
        task_func('source_dir', 'invalid_target_dir')