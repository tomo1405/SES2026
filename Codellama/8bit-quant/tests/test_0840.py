import csv

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
            assert row['Name'] in ['ABCDE', 'FGHIJ', 'KLMNO', 'PQRST', 'UVWXY']
            assert row['Age'] in range(20, 61)
            assert row['Gender'] in gender
            assert row['Country'] in countries