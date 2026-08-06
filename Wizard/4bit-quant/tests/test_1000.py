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
    url = "https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.csv"
    column_name = "imdb_rating"
    csv_file_path = "movies.csv"

    # Test case 1: Valid column name
    result = task_func(url, column_name, csv_file_path)
    assert result == collections.Counter({'8.3': 1, '8.4': 1, '8.5': 1, '8.6': 1, '8.7': 1, '8.8': 1, '8.9': 1, '9.0': 1, '9.1': 1, '9.2': 1, '9.3': 1, '9.4': 1, '9.5': 1, '9.6': 1, '9.7': 1, '9.8': 1, '9.9': 1})

    # Test case 2: Invalid column name
    with pytest.raises(ValueError):
        task_func(url, "invalid_column_name", csv_file_path)

    # Test case 3: Invalid URL
    with pytest.raises(urllib.error.URLError):
        task_func("invalid_url", column_name, csv_file_path)

    # Test case 4: Invalid CSV file path
    with pytest.raises(FileNotFoundError):
        task_func(url, column_name, "invalid_csv_file_path")