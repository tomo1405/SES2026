import pytest
from src_0995 import task_func

def test_task_func():
    url = "https://example.com"
    csv_file_path = "output.csv"
    expected_output = [("Title 1", "Date 1", "Author 1"), ("Title 2", "Date 2", "Author 2")]

    data = task_func(url, csv_file_path)

    assert data == expected_output
    assert len(data) == 2
    assert data[0] == ("Title 1", "Date 1", "Author 1")
    assert data[1] == ("Title 2", "Date 2", "Author 2")

if __name__ == "__main__":
    pytest.main()