import pytest
from src_1107 import task_func

def test_task_func_valid_file():
    # Test with a valid file path
    file_path = 'test_file.txt'
    with open(file_path, 'w') as f:
        f.write('test')
    try:
        result = task_func(file_path)
        assert result == datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    finally:
        os.remove(file_path)

def test_task_func_invalid_file():
    # Test with an invalid file path
    file_path = 'nonexistent_file.txt'
    with pytest.raises(FileNotFoundError):
        task_func(file_path)