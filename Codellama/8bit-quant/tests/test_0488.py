import pytest
from src_0488 import task_func

def test_task_func_valid_file():
    file_path = "test_data.txt"
    df = task_func(file_path)
    assert df.shape == (3, 3)
    assert df.columns.tolist() == ["Timestamp", "Level", "Message"]
    assert df["Timestamp"].dtype == "datetime64[ns]"
    assert df["Level"].dtype == "object"
    assert df["Message"].dtype == "object"

def test_task_func_invalid_file():
    file_path = "invalid_file.txt"
    with pytest.raises(FileNotFoundError):
        task_func(file_path)

def test_task_func_empty_file():
    file_path = "empty_file.txt"
    df = task_func(file_path)
    assert df.shape == (0, 3)
    assert df.columns.tolist() == ["Timestamp", "Level", "Message"]
    assert df["Timestamp"].dtype == "datetime64[ns]"
    assert df["Level"].dtype == "object"
    assert df["Message"].dtype == "object"