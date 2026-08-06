import pytest
from src_0580 import task_func

def test_task_func():
    csv_file = "example.csv"
    ax, most_common_words = task_func(csv_file)
    assert ax is not None
    assert most_common_words is not None
    assert len(most_common_words) == 10

def test_task_func_file_not_found():
    csv_file = "nonexistent.csv"
    with pytest.raises(FileNotFoundError):
        task_func(csv_file)

def test_task_func_io_error():
    csv_file = "invalid_file.csv"
    with pytest.raises(IOError):
        task_func(csv_file)