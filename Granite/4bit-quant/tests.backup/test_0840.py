import csv
import random
import pytest

from src_0840 import task_func

def test_task_func():
    file_path = 'test.csv'
    num_rows = 10
    seed = 42
    gender = ['Male', 'Female', 'Non-Binary']
    countries = ['USA', 'UK', 'Canada', 'Australia', 'India']

    task_func(file_path, num_rows, gender, countries, seed)

    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)

    assert len(rows) == num_rows
    for row in rows:
        assert row['Name']
        assert 20 <= int(row['Age']) <= 60
        assert row['Gender'] in gender
        assert row['Country'] in countries