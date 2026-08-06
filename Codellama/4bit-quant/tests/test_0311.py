import csv
import os

import pytest
from src_0311 import task_func


def test_task_func():
    filename = 'test_data.csv'
    filepath = task_func(filename)
    assert filepath == os.path.join(os.getcwd(), filename)

    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        assert header == COLUMNS

        data = [row for row in reader]
        assert len(data) == PEOPLE_COUNT

        for row in data:
            assert len(row) == 4
            assert row[0].startswith('Person_')
            assert row[1] >= 20 and row[1] <= 50
            assert row[2] >= 150 and row[2] <= 200
            assert row[3] >= 50 and row[3] <= 100

        averages = data[-1]
        assert averages[0] == 'Average'
        assert averages[1] == pytest.approx(mean([row[1] for row in data]))
        assert averages[2] == pytest.approx(mean([row[2] for row in data]))
        assert averages[3] == pytest.approx(mean([row[3] for row in data]))