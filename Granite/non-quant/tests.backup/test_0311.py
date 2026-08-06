import os
import csv
import random
from statistics import mean
from src_0311 import task_func
import pytest

def test_task_func():
    filename = 'test_file.csv'
    filepath = task_func(filename)
    assert os.path.exists(filepath)
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        columns = next(reader)
        assert columns == COLUMNS
        data = [row for row in reader]
        assert len(data) == PEOPLE_COUNT
        averages = data[-1]
        assert averages[0] == 'Average'
        assert averages[1] == mean([row[1] for row in data])
        assert averages[2] == mean([row[2] for row in data])
        assert averages[3] == mean([row[3] for row in data])