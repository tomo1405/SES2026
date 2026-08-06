python
import csv
import random
import pytest

def task_func(file_path, num_rows, gender=['Male', 'Female', 'Non-Binary'], countries=['USA', 'UK', 'Canada', 'Australia', 'India'], seed=None):
    FIELDS = ['Name', 'Age', 'Gender', 'Country']
    random.seed(seed)

    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=FIELDS)
        writer.writeheader()

        for _ in range(num_rows):
            writer.writerow({
                'Name': ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=5)),
                'Age': random.randint(20, 60),
                'Gender': random.choice(gender),
                'Country': random.choice(countries)
            })

    return file_path

def test_task_func():
    file_path = 'test.csv'
    num_rows = 10
    gender = ['Male', 'Female', 'Non-Binary']
    countries = ['USA', 'UK', 'Canada', 'Australia', 'India']
    seed = 42

    task_func(file_path, num_rows, gender, countries, seed)

    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        rows = [row for row in reader]

    assert len(rows) == num_rows
    assert set(rows[0].keys()) == set(FIELDS)
    assert set(rows[0].values()) == set(['Name', 'Age', 'Gender', 'Country'])
    assert set(rows[0]['Gender']) in set(gender)
    assert set(rows[0]['Country']) in set(countries)

    for row in rows:
        assert isinstance(row['Name'], str)
        assert isinstance(row['Age'], int)
        assert isinstance(row['Gender'], str)
        assert isinstance(row['Country'], str)

    assert rows[0]['Name'] == 'EGHI'
    assert rows[0]['Age'] == 27
    assert rows[0]['Gender'] == 'Male'
    assert rows[0]['Country'] == 'USA'

    assert rows[1]['Name'] == 'FGHI'
    assert rows[1]['Age'] == 32
    assert rows[1]['Gender'] == 'Female'
    assert rows[1]['Country'] == 'UK'

    assert rows[2]['Name'] == 'GABC'
    assert rows[2]['Age'] == 41
    assert rows[2]['Gender'] == 'Non-Binary'
    assert rows[2]['Country'] == 'Canada'

    assert rows[3]['Name'] == 'HABC'
    assert rows[3]['Age'] == 29
    assert rows[3]['Gender'] == 'Male'
    assert rows[3]['Country'] == 'Australia'

    assert rows[4]['Name'] == 'IJKL'
    assert rows[4]['Age'] == 35
    assert rows[4]['Gender'] == 'Female'
    assert rows[4]['Country'] == 'India'

    assert rows[5]['Name'] == 'JKLM'
    assert rows[5]['Age'] == 25
    assert rows[5]['Gender'] == 'Male'
    assert rows[5]['Country'] == 'USA'

    assert rows[6]['Name'] == 'KLMN'
    assert rows[6]['Age'] == 30
    assert rows[6]['Gender'] == 'Female'
    assert rows[6]['Country'] == 'UK'

    assert rows[7]['Name'] == 'MNOP'
    assert rows[7]['Age'] == 40
    assert rows[7]['Gender'] == 'Non-Binary'
    assert rows[7]['Country'] == 'Canada'

    assert rows[8]['Name'] == 'OPQR'
    assert rows[8]['Age'] == 30
    assert rows[8]['Gender'] == 'Male'
    assert rows[8]['Country'] == 'Australia'

    assert rows[9]['Name'] == 'QRST'
    assert rows[9]['Age'] == 35
    assert rows[9]['Gender'] == 'Female'
    assert rows[9]['Country'] == 'India'

    import os
    os.remove(file_path)