import csv

from src_1113 import task_func


def test_task_func():
    file_name = task_func()
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        assert header == ['Time'] + DATA
        for row in reader:
            time = row[0]
            for i, data_type in enumerate(DATA):
                min_val, max_val = RANGE[data_type]
                value = row[i+1]
                assert min_val <= value <= max_val