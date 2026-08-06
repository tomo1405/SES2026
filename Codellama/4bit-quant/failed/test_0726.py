import pytest
from src_0726 import task_func

def test_task_func():
    # Test with default arguments
    task_func()
    assert os.path.exists('./files/file1.txt')
    assert os.path.exists('./files/file2.txt')
    assert os.path.exists('./files/file3.txt')

    # Test with custom arguments
    task_func(directory='./test_files/', from_encoding='cp1251', to_encoding='utf8')
    assert os.path.exists('./test_files/file1.txt')
    assert os.path.exists('./test_files/file2.txt')
    assert os.path.exists('./test_files/file3.txt')

    # Test with invalid arguments
    with pytest.raises(ValueError):
        task_func(directory='./invalid_directory/', from_encoding='cp1251', to_encoding='utf8')