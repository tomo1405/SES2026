import pytest
from src_0995 import task_func

def test_task_func():
    url = "https://www.example.com"
    csv_file_path = "test_data.csv"
    data = task_func(url, csv_file_path)
    assert data == [("Title 1", "Date 1", "Author 1"), ("Title 2", "Date 2", "Author 2")]

def test_task_func_with_invalid_url():
    url = "https://www.example.com/invalid"
    csv_file_path = "test_data.csv"
    with pytest.raises(RuntimeError):
        task_func(url, csv_file_path)

def test_task_func_with_invalid_csv_file_path():
    url = "https://www.example.com"
    csv_file_path = "invalid_path.csv"
    with pytest.raises(FileNotFoundError):
        task_func(url, csv_file_path)