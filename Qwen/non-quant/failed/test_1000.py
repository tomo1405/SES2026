import pytest
from src_1000 import task_func
import os
import csv
from unittest.mock import patch

@pytest.fixture
def mock_csv_data(tmpdir):
    data = """name,age
Alice,30
Bob,25
Charlie,30
"""
    csv_file = tmpdir.join("test.csv")
    with open(csv_file.strpath, "w", newline='') as f:
        f.write(data)
    return csv_file.strpath

@pytest.fixture
def mock_urlretrieve(tmpdir):
    def side_effect(url, filename):
        with open(filename, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["name", "age"])
            writer.writerow(["Alice", 30])
            writer.writerow(["Bob", 25])
            writer.writerow(["Charlie", 30])
    return side_effect

@patch('src_1000.urllib.request.urlretrieve', side_effect=mock_urlretrieve)
def test_task_func(mock_urlretrieve, tmpdir):
    url = "http://example.com/data.csv"
    column_name = "age"
    csv_file_path = tmpdir.join("data.csv").strpath

    result = task_func(url, column_name, csv_file_path)

    assert result == collections.Counter({30: 2, 25: 1})
    assert not os.path.exists(csv_file_path)

@patch('src_1000.urllib.request.urlretrieve', side_effect=mock_urlretrieve)
def test_task_func_missing_column(mock_urlretrieve, tmpdir):
    url = "http://example.com/data.csv"
    column_name = "gender"
    csv_file_path = tmpdir.join("data.csv").strpath

    with pytest.raises(ValueError) as excinfo:
        task_func(url, column_name, csv_file_path)

    assert str(excinfo.value) == "The provided column_name 'gender' does not exist in the CSV file."
    assert not os.path.exists(csv_file_path)