import csv
from typing import Counter

import pytest
from src_0529 import task_func


@pytest.fixture
def create_csv_file(tmpdir):
    file_path = tmpdir.join("test.csv")
    with open(file_path, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age"])
        writer.writerow(["Alice", 30])
        writer.writerow(["Bob", 25])
        writer.writerow(["Alice", 30])  # Duplicate
    return str(file_path)

def test_task_func_valid_file(create_csv_file):
    duplicates, ax = task_func(create_csv_file)
    assert isinstance(duplicates, Counter)
    assert duplicates == Counter({('Alice', 30): 2})
    assert ax is not None

def test_task_func_invalid_file_extension(tmpdir):
    file_path = tmpdir.join("test.txt")
    with open(file_path, "w") as f:
        f.write("This is not a CSV file.")
    with pytest.raises(ValueError) as excinfo:
        task_func(str(file_path))
    assert "Invalid file format. Only .csv files are accepted." in str(excinfo.value)

def test_task_func_no_duplicates(create_csv_file):
    # Remove the duplicate row
    with open(create_csv_file, "r") as f:
        lines = f.readlines()
    with open(create_csv_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(lines[0].strip().split(","))
        writer.writerow(lines[1].strip().split(","))

    duplicates, ax = task_func(create_csv_file)
    assert isinstance(duplicates, Counter)
    assert duplicates == Counter()
    assert ax is None

def test_task_func_empty_file(tmpdir):
    file_path = tmpdir.join("empty.csv")
    with open(file_path, "w", newline='') as f:
        pass  # Create an empty file
    duplicates, ax = task_func(str(file_path))
    assert isinstance(duplicates, Counter)
    assert duplicates == Counter()
    assert ax is None