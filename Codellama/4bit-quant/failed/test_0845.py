import pytest
from src_0845 import task_func

def test_task_func():
    file_path = 'test_data.csv'
    num_rows = 10
    random_seed = 42
    result = task_func(file_path, num_rows, random_seed)
    assert result == file_path
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        assert header == ['Name', 'Age', 'Address', 'Email']
        for row in reader:
            assert len(row) == 4
            assert row[0] == fake.name()
            assert row[1] == str(random.randint(20, 60))
            assert row[2] == fake.address().replace('\n', ', ')
            assert row[3] == fake.email()
    os.remove(file_path)