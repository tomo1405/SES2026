import pytest
from src_0510 import task_func

def test_task_func():
    file_path1 = "path/to/file1.csv"
    file_path2 = "path/to/file2.csv"
    delimiter = ","
    quotechar = '"'
    df = task_func(file_path1, file_path2, delimiter, quotechar)
    assert isinstance(df, pd.DataFrame)
    assert df.columns.tolist() == ['Line Number', 'Status', 'Content']

def test_task_func_file_not_found():
    file_path1 = "path/to/file1.csv"
    file_path2 = "path/to/file2.csv"
    delimiter = ","
    quotechar = '"'
    with pytest.raises(FileNotFoundError):
        task_func(file_path1, file_path2, delimiter, quotechar)

def test_task_func_empty_file():
    file_path1 = "path/to/empty_file1.csv"
    file_path2 = "path/to/empty_file2.csv"
    delimiter = ","
    quotechar = '"'
    with pytest.raises(ValueError):
        task_func(file_path1, file_path2, delimiter, quotechar)

def test_task_func_other_error():
    file_path1 = "path/to/file1.csv"
    file_path2 = "path/to/file2.csv"
    delimiter = ","
    quotechar = '"'
    with pytest.raises(Exception):
        task_func(file_path1, file_path2, delimiter, quotechar)