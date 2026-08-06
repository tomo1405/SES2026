import pytest
from src_1053 import task_func

def test_task_func_with_valid_input():
    file_path = "path/to/file.csv"
    save_path = "path/to/save/plot.png"
    ax = task_func(file_path, save_path)
    assert ax is not None

def test_task_func_with_invalid_input():
    file_path = "path/to/file.csv"
    save_path = None
    ax = task_func(file_path, save_path)
    assert ax is None

def test_task_func_with_empty_dataframe():
    file_path = "path/to/empty/file.csv"
    save_path = "path/to/save/plot.png"
    ax = task_func(file_path, save_path)
    assert ax is None

def test_task_func_with_stop_words():
    file_path = "path/to/file.csv"
    save_path = "path/to/save/plot.png"
    ax = task_func(file_path, save_path)
    assert ax is not None
    assert len(ax.get_xticklabels()) == 10
    assert all(label.get_text() in STOP_WORDS for label in ax.get_xticklabels())