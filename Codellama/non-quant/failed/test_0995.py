import pytest
from src_0995 import task_func


def test_task_func_valid_url():
    url = "https://www.example.com"
    csv_file_path = "test_data.csv"
    data = task_func(url, csv_file_path)
    assert data == [("No Title", "No Date", "No Author")]


def test_task_func_invalid_url():
    url = "https://www.example.com/invalid"
    csv_file_path = "test_data.csv"
    with pytest.raises(RuntimeError):
        task_func(url, csv_file_path)


def test_task_func_valid_csv_file_path():
    url = "https://www.example.com"
    csv_file_path = "test_data.csv"
    data = task_func(url, csv_file_path)
    assert data == [("No Title", "No Date", "No Author")]
    assert pd.read_csv(csv_file_path) == pd.DataFrame(data, columns=["Title", "Date", "Author"])


def test_task_func_invalid_csv_file_path():
    url = "https://www.example.com"
    csv_file_path = "invalid_path.csv"
    with pytest.raises(FileNotFoundError):
        task_func(url, csv_file_path)