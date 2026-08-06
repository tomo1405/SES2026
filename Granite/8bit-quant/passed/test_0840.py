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

    random.seed(seed)
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['Name', 'Age', 'Gender', 'Country'])
        writer.writeheader()

        for _ in range(num_rows):
            writer.writerow({
                'Name': ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=5)),
                'Age': random.randint(20, 60),
                'Gender': random.choice(gender),
                'Country': random.choice(countries)
            })

    result = task_func(file_path, num_rows, gender, countries, seed)
    assert result == 'test.csv'