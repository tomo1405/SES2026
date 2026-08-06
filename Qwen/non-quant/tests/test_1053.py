import pytest
from src_1053 import task_func
import pandas as pd
from io import StringIO

def test_task_func_with_valid_data(tmpdir):
    data = "Hello world\nThis is a test\nAnother line"
    file_path = tmpdir.join("test.csv")
    file_path.write(data)

    result = task_func(str(file_path))
    assert isinstance(result, pd.Series)
    assert len(result) == 10

def test_task_func_with_empty_data(tmpdir, capsys):
    data = ""
    file_path = tmpdir.join("empty.csv")
    file_path.write(data)

    result = task_func(str(file_path))
    captured = capsys.readouterr()
    assert captured.out == "No valid words to plot. Returning None.\n"
    assert result is None

def test_task_func_with_only_stop_words(tmpdir, capsys):
    data = "a an the in on at and or"
    file_path = tmpdir.join("stop_words.csv")
    file_path.write(data)

    result = task_func(str(file_path))
    captured = capsys.readouterr()
    assert captured.out == "No valid words to plot. Returning None.\n"
    assert result is None

def test_task_func_with_save_path(tmpdir):
    data = "Hello world\nThis is a test\nAnother line"
    file_path = tmpdir.join("test.csv")
    file_path.write(data)
    save_path = str(tmpdir.join("plot.png"))

    result = task_func(str(file_path), save_path=save_path)
    assert result is None
    assert tmpdir.join("plot.png").exists()

def test_task_func_with_no_save_path(tmpdir):
    data = "Hello world\nThis is a test\nAnother line"
    file_path = tmpdir.join("test.csv")
    file_path.write(data)

    result = task_func(str(file_path))
    assert isinstance(result, pd.Series)
    assert len(result) == 10