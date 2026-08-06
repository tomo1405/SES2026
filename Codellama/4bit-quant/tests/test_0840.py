import csv
import random

from src_0840 import task_func


def test_task_func():
    file_path = 'test_data.csv'
    num_rows = 10
    gender = ['Male', 'Female', 'Non-Binary']
    countries = ['USA', 'UK', 'Canada', 'Australia', 'India']
    seed = 1234

    result = task_func(file_path, num_rows, gender, countries, seed)

    assert result == file_path

    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            assert row['Name'] in [''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=5))]
            assert row['Age'] in [random.randint(20, 60)]
            assert row['Gender'] in [random.choice(gender)]
            assert row['Country'] in [random.choice(countries)]