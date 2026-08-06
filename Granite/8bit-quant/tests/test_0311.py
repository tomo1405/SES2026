import csv
import os
from statistics import mean

import pytest
from src_0311 import task_func


def test_task_func():
    filename = 'test_file.csv'
    filepath = task_func(filename)

    # Check if the file was created
    assert os.path.exists(filepath)

    # Check if the file has the correct columns
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        assert next(reader) == COLUMNS

    # Check if the file has the correct number of rows
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        assert len(rows) == PEOPLE_COUNT + 1

    # Check if the averages are correct
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        averages = rows[-1]
        assert averages[0] == 'Average'
        assert averages[1] == mean([row[1] for row in rows[1:-1]])
        assert averages[2] == mean([row[2] for row in rows[1:-1]])
        assert averages[3] == mean([row[3] for row in rows[1:-1]])

if __name__ == '__main__':
    pytest.main()