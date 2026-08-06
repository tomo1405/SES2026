import pytest
from src_0488 import task_func

def test_task_func_valid_file():
    file_path = "test_data.txt"
    df = task_func(file_path)
    assert df.shape == (3, 3)
    assert df.columns.tolist() == ["Timestamp", "Level", "Message"]
    assert df["Timestamp"].tolist() == ["2022-01-01 00:00:00.000000", "2022-01-01 00:00:01.000000", "2022-01-01 00:00:02.000000"]
    assert df["Level"].tolist() == ["INFO", "WARNING", "ERROR"]
    assert df["Message"].tolist() == ["This is an info message", "This is a warning message", "This is an error message"]

def test_task_func_invalid_file():
    file_path = "invalid_file.txt"
    with pytest.raises(FileNotFoundError):
        task_func(file_path)