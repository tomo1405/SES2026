python
import pytest
from src_0940 import task_func

def test_task_func():
    # Test case 1: Valid input
    dir_path = 'test_dir'
    os.mkdir(dir_path)
    open(os.path.join(dir_path, 'file1.txt'), 'w').close()
    open(os.path.join(dir_path, 'file2.txt'), 'w').close()
    new_names = task_func(dir_path)
    assert new_names == ['file1', 'file2']
    assert os.path.exists(os.path.join(dir_path, 'file1'))
    assert os.path.exists(os.path.join(dir_path, 'file2'))
    os.rmdir(dir_path)

    # Test case 2: Invalid input (empty string)
    with pytest.raises(ValueError):
        task_func('')

    # Test case 3: Invalid input (non-existent directory)
    with pytest.raises(FileNotFoundError):
        task_func('non_existent_dir')

    # Test case 4: Invalid input (directory with non-text files)
    os.mkdir(dir_path)
    open(os.path.join(dir_path, 'file1.txt'), 'w').close()
    open(os.path.join(dir_path, 'file2.txt'), 'w').close()
    open(os.path.join(dir_path, 'file3.jpg'), 'w').close()
    with pytest.raises(ValueError):
        task_func(dir_path)
    os.rmdir(dir_path)