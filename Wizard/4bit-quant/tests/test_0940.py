python
import pytest
from src_0940 import task_func

def test_task_func():
    # Test case 1: Valid input
    dir_path = 'test_dir'
    os.mkdir(dir_path)
    with open(os.path.join(dir_path, 'test_file.txt'), 'w') as f:
        f.write('test content')
    assert task_func(dir_path) == ['test_file']
    os.remove(os.path.join(dir_path, 'test_file.txt'))
    os.rmdir(dir_path)

    # Test case 2: Invalid input (empty directory)
    dir_path = 'test_dir'
    os.mkdir(dir_path)
    assert task_func(dir_path) == []
    os.rmdir(dir_path)

    # Test case 3: Invalid input (non-existent directory)
    dir_path = 'non_existent_dir'
    with pytest.raises(FileNotFoundError):
        task_func(dir_path)