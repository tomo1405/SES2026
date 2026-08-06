import csv
import random
from faker import Faker
from src_0845 import task_func
import pytest

def test_task_func():
    file_path = 'test.csv'
    num_rows = 10
    random_seed = 42

    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Name', 'Age', 'Address', 'Email'])
        for _ in range(num_rows):
            name = Faker().name()
            age = random.randint(20, 60)
            address = Faker().address().replace('\n', ', ')
            email = Faker().email()
            writer.writerow([name, age, address, email])

    result = task_func(file_path, num_rows, random_seed)

    assert result == 'test.csv'

def test_task_func_invalid_num_rows():
    file_path = 'test.csv'
    num_rows = -1
    random_seed = 42

    with pytest.raises(ValueError) as excinfo:
        task_func(file_path, num_rows, random_seed)

    assert 'num_rows should be an integer >=0.' in str(excinfo.value)