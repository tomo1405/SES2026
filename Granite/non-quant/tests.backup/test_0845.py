import pytest
from src_0845 import task_func

def test_task_func():
    file_path = 'test.csv'
    num_rows = 10
    random_seed = 42

    result = task_func(file_path, num_rows, random_seed)

    assert result == 'test.csv'
    assert os.path.exists(result)
    with open(result, 'r') as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)
        assert len(rows) == num_rows
        for row in rows:
            assert len(row) == 4
            assert row[0]  # Name is not empty
            assert 20 <= int(row[1]) <= 60  # Age is between 20 and 60
            assert row[2]  # Address is not empty
            assert row[3]  # Email is not empty

test_task_func()