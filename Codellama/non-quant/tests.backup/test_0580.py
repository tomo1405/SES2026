import pytest
from src_0580 import task_func

def test_task_func_valid_csv_file():
    csv_file = "test_data.csv"
    ax, most_common_words = task_func(csv_file)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert isinstance(most_common_words, list)
    assert len(most_common_words) == 10

def test_task_func_invalid_csv_file():
    csv_file = "invalid_file.csv"
    with pytest.raises(FileNotFoundError):
        task_func(csv_file)

def test_task_func_io_error():
    csv_file = "test_data.csv"
    with pytest.raises(IOError):
        task_func(csv_file)