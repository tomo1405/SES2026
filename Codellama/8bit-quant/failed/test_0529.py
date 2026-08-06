import pytest
from src_0529 import task_func

def test_task_func_valid_csv():
    file_path = "test_data.csv"
    duplicates, ax = task_func(file_path)
    assert duplicates == Counter({('a', 'b'): 2, ('c', 'd'): 3})
    assert ax is not None

def test_task_func_invalid_csv():
    file_path = "test_data.txt"
    with pytest.raises(ValueError):
        task_func(file_path)