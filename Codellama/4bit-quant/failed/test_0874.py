import pytest
from src_0874 import task_func

def test_task_func():
    data = [
        ['Name', 'Age', 'Gender'],
        ['Alice', 25, 'Female'],
        ['Bob', 30, 'Male'],
        ['Charlie', 35, 'Male']
    ]
    file_path = 'test_data.csv'
    headers = ['Name', 'Age', 'Gender']
    result = task_func(data, file_path, headers)
    assert result == os.path.abspath(file_path)

    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        assert rows[0] == headers
        assert rows[1] == ['Alice', 25, 'Female']
        assert rows[2] == ['Bob', 30, 'Male']
        assert rows[3] == ['Charlie', 35, 'Male']