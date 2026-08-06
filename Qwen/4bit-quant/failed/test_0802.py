import pytest
from src_0802 import task_func

def test_task_func_empty_file(tmp_path):
    file_path = tmp_path / "empty.csv"
    file_path.write_text("")
    result = task_func(str(file_path))
    assert result == {}

def test_task_func_single_row(tmp_path):
    file_path = tmp_path / "single_row.csv"
    file_path.write_text("col1,col2\n1,2")
    result = task_func(str(file_path))
    assert result == {'col1': 1, 'col2': 2}

def test_task_func_multiple_rows(tmp_path):
    file_path = tmp_path / "multiple_rows.csv"
    file_path.write_text("col1,col2\n1,2\n1,3\n1,2")
    result = task_func(str(file_path))
    assert result == {'col1': 1, 'col2': 2}

def test_task_func_tie_breaker(tmp_path):
    file_path = tmp_path / "tie_breaker.csv"
    file_path.write_text("col1,col2\n1,2\n2,2\n1,3\n1,2")
    result = task_func(str(file_path))
    assert result == {'col1': 1, 'col2': 2}

def test_task_func_non_numeric_data(tmp_path):
    file_path = tmp_path / "non_numeric.csv"
    file_path.write_text("col1,col2\na,b\na,c\na,b")
    result = task_func(str(file_path))
    assert result == {'col1': 'a', 'col2': 'b'}