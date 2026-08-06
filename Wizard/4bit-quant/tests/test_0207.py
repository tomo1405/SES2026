python
import csv
import json
import os
import pytest

def task_func(file_name):
    if not os.path.exists(file_name):
        raise FileNotFoundError("File does not exist.")

    data = []

    with open(file_name, 'r') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            data.append(row)

    json_file_name = file_name.split('.')[0] + '.json'

    with open(json_file_name, 'w') as f:
        json.dump(data, f)

    return json_file_name

def test_task_func():
    # Test case 1: File does not exist
    with pytest.raises(FileNotFoundError):
        task_func('non_existent_file.csv')

    # Test case 2: Valid CSV file
    csv_file_name = 'test_file.csv'
    with open(csv_file_name, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'age'])
        writer.writerow(['John', '30'])
        writer.writerow(['Jane', '25'])

    json_file_name = task_func(csv_file_name)
    assert os.path.exists(json_file_name)
    with open(json_file_name, 'r') as f:
        data = json.load(f)
    assert data == [{'name': 'John', 'age': '30'}, {'name': 'Jane', 'age': '25'}]
    os.remove(csv_file_name)
    os.remove(json_file_name)

    # Test case 3: Invalid CSV file
    invalid_csv_file_name = 'invalid_file.csv'
    with open(invalid_csv_file_name, 'w') as f:
        f.write('name,age\nJohn,30\nJane,25\n')

    with pytest.raises(csv.Error):
        task_func(invalid_csv_file_name)
    os.remove(invalid_csv_file_name)