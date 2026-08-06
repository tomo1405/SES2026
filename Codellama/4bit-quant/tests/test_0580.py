import pytest
from src_0580 import task_func

def test_task_func():
    csv_file = "test_data.csv"
    ax, most_common_words = task_func(csv_file)
    assert ax is not None
    assert most_common_words is not None
    assert len(most_common_words) == 10
    assert all(isinstance(word, str) for word, count in most_common_words)
    assert all(isinstance(count, int) for word, count in most_common_words)

def test_task_func_invalid_file():
    csv_file = "invalid_file.csv"
    with pytest.raises(FileNotFoundError):
        task_func(csv_file)

def test_task_func_invalid_data():
    csv_file = "test_data_invalid.csv"
    with pytest.raises(IOError):
        task_func(csv_file)