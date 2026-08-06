python
import csv
import random
from faker import Faker
import pytest

def task_func(file_path, num_rows, random_seed=None):

    if num_rows < 0 or not isinstance(num_rows, int):
        raise ValueError('num_rows should be an integer >=0.')

    fake = Faker()
    fake.seed_instance(random_seed)
    random.seed(random_seed)
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Name', 'Age', 'Address', 'Email'])
        for _ in range(num_rows):
            name = fake.name()
            age = random.randint(20, 60)
            address = fake.address().replace('\n', ', ')
            email = fake.email()
            writer.writerow([name, age, address, email])
    return file_path

def test_task_func():
    file_path = 'test.csv'
    num_rows = 10
    random_seed = 42
    task_func(file_path, num_rows, random_seed)
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        assert header == ['Name', 'Age', 'Address', 'Email']
        for i, row in enumerate(reader):
            assert len(row) == 4
            assert isinstance(row[0], str)
            assert isinstance(row[1], int)
            assert isinstance(row[2], str)
            assert '@' in row[3]
    assert i+1 == num_rows