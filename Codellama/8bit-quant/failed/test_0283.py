import pytest
from src_0283 import task_func

def test_task_func_valid_file_path():
    file_path = 'path/to/file.jpg'
    onpick = lambda event: print(event.artist.get_label())
    ax = task_func(file_path, onpick)
    assert ax is not None

def test_task_func_invalid_file_path():
    file_path = 'path/to/invalid/file.jpg'
    onpick = lambda event: print(event.artist.get_label())
    with pytest.raises(FileNotFoundError):
        task_func(file_path, onpick)