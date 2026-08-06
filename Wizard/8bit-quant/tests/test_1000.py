python
import urllib.request
import os
import csv
import collections
import pytest

def task_func(url, column_name, csv_file_path):
    urllib.request.urlretrieve(url, csv_file_path)

    with open(csv_file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if column_name not in reader.fieldnames:
            os.remove(csv_file_path)
            raise ValueError(
                f"The provided column_name '{column_name}' does not exist in the CSV file."
            )
        values = [row[column_name] for row in reader]

    os.remove(csv_file_path)

    return collections.Counter(values)

def test_task_func():
    url = "https://example.com/data.csv"
    column_name = "column_1"
    csv_file_path = "data.csv"

    # Test case 1: Valid CSV file with valid column name
    with open(csv_file_path, "w", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["column_1", "column_2"])
        writer.writeheader()
        writer.writerow({"column_1": "value_1", "column_2": "value_2"})
        writer.writerow({"column_1": "value_3", "column_2": "value_4"})

    result = task_func(url, column_name, csv_file_path)
    assert result == {"value_1": 1, "value_3": 1}

    # Test case 2: Valid CSV file with invalid column name
    with open(csv_file_path, "w", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["column_1", "column_2"])
        writer.writeheader()
        writer.writerow({"column_1": "value_1", "column_2": "value_2"})
        writer.writerow({"column_1": "value_3", "column_2": "value_4"})

    with pytest.raises(ValueError):
        task_func(url, "invalid_column_name", csv_file_path)

    # Test case 3: Invalid CSV file
    with open(csv_file_path, "w", encoding="utf-8") as f:
        f.write("invalid_csv_data")

    with pytest.raises(csv.Error):
        task_func(url, column_name, csv_file_path)

    # Test case 4: Non-existent CSV file
    with pytest.raises(FileNotFoundError):
        task_func(url, column_name, "nonexistent_file.csv")

    # Clean up
    os.remove(csv_file_path)