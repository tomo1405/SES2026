import pytest
from src_0488 import task_func

def test_task_func_valid_file():
    file_path = "path/to/valid/file.txt"
    df = task_func(file_path)
    assert df.shape == (3, 3)
    assert df.columns.tolist() == ["Timestamp", "Level", "Message"]
    assert df.dtypes.tolist() == [np.datetime64, np.object, np.object]

def test_task_func_invalid_file():
    file_path = "path/to/invalid/file.txt"
    with pytest.raises(FileNotFoundError):
        task_func(file_path)

def test_task_func_empty_file():
    file_path = "path/to/empty/file.txt"
    df = task_func(file_path)
    assert df.empty
    assert df.columns.tolist() == ["Timestamp", "Level", "Message"]
    assert df.dtypes.tolist() == [np.datetime64, np.object, np.object]