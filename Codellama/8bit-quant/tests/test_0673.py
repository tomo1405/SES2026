import csv

from src_0673 import task_func


def test_task_func_valid_input():
    filename = "test_data.csv"
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerows([[1, 2, 3], [4, 5, 6]])

    result = task_func(filename)

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    assert rows == [[6, 5, 4], [3, 2, 1]]

def test_task_func_invalid_input():
    filename = "test_data.csv"
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerows([[1, 2, 3], [4, 5, 6]])

    result = task_func(filename)

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    assert rows == [[6, 5, 4], [3, 2, 1]]

def test_task_func_exception():
    filename = "test_data.csv"
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerows([[1, 2, 3], [4, 5, 6]])

    result = task_func(filename)

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    assert rows == [[6, 5, 4], [3, 2, 1]]