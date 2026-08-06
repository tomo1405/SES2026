python
import csv
import random
import pytest

from src_0840 import task_func

def test_task_func():
    file_path = 'test.csv'
    num_rows = 10
    gender = ['Male', 'Female', 'Non-Binary']
    countries = ['USA', 'UK', 'Canada', 'Australia', 'India']
    seed = 42

    task_func(file_path, num_rows, gender, countries, seed)

    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        rows = [row for row in reader]

    assert len(rows) == num_rows
    assert all(row['Name'] and row['Age'] and row['Gender'] and row['Country'] for row in rows)
    assert all(row['Gender'] in gender for row in rows)
    assert all(row['Country'] in countries for row in rows)
    assert all(row['Age'] >= 20 and row['Age'] <= 60 for row in rows)

    # cleanup
    import os
    os.remove(file_path)