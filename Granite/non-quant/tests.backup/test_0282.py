import pytest
from src_0282 import task_func

def test_task_func():
    folder_path = "path/to/folder"
    expected_result = {"192.168.1.1": 1, "10.0.0.1": 2, "172.16.0.1": 1}
    result = task_func(folder_path)
    assert result == expected_result, "Task function returned an incorrect result"

def test_task_func_with_empty_folder():
    folder_path = "path/to/empty/folder"
    expected_result = {}
    result = task_func(folder_path)
    assert result == expected_result, "Task function returned an incorrect result for an empty folder"

def test_task_func_with_invalid_folder_path():
    folder_path = "path/to/invalid/folder"
    with pytest.raises(FileNotFoundError):
        task_func(folder_path)