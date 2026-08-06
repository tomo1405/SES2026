import pytest
from src_0580 import task_func

def test_task_func_with_valid_csv_file():
    csv_file = "valid_file.csv"
    ax, most_common_words = task_func(csv_file)
    assert ax is not None
    assert most_common_words is not None

def test_task_func_with_invalid_csv_file():
    csv_file = "invalid_file.csv"
    with pytest.raises(FileNotFoundError):
        task_func(csv_file)

def test_task_func_with_io_error():
    csv_file = "file_with_io_error.csv"
    with pytest.raises(IOError):
        task_func(csv_file)