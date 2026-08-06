import pytest
from src_0782 import task_func

def test_task_func_valid_filepath():
    filepath = 'test_file.txt'
    expected_result = {'size': '100 bytes', 'last_modified': '2022-02-22 12:34:56'}
    with open(filepath, 'w') as f:
        f.write('test')
    result = task_func(filepath)
    assert result == expected_result

def test_task_func_invalid_filepath():
    filepath = 'invalid_file.txt'
    with pytest.raises(Exception) as e:
        task_func(filepath)
    assert str(e) == f"Error: [Errno 2] No such file or directory: '{filepath}'"