import pytest
from src_1107 import task_func

def test_task_func_valid_file():
    file_path = 'test_file.txt'
    with open(file_path, 'w') as f:
        f.write('test')
    assert task_func(file_path) == datetime.fromtimestamp(os.path.getctime(file_path)).strftime(DATE_FORMAT)

def test_task_func_invalid_file():
    file_path = 'invalid_file.txt'
    with pytest.raises(FileNotFoundError):
        task_func(file_path)