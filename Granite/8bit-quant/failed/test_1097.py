import pytest
from src_1097 import task_func

def test_task_func():
    text = "This is a test. It has a $dollar sign in it."
    filename = "test_file.csv"
    result = task_func(text, filename)
    assert result == os.path.abspath(filename)
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
        assert rows == [['Word'], ['dollar']]

def test_task_func_no_dollar():
    text = "This is a test. It does not have a $dollar sign in it."
    filename = "test_file.csv"
    result = task_func(text, filename)
    assert result == os.path.abspath(filename)
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
        assert rows == [['Word']]

def test_task_func_empty_string():
    text = ""
    filename = "test_file.csv"
    result = task_func(text, filename)
    assert result == os.path.abspath(filename)
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
        assert rows == [['Word']]