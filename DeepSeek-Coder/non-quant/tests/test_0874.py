import pytest
from src_0874 import task_func

@pytest.fixture
def sample_data():
    return [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25}
    ]

@pytest.fixture
def sample_headers():
    return ['name', 'age']

def test_task_func(tmp_path, sample_data, sample_headers):
    file_path = tmp_path / "test.csv"
    result = task_func(sample_data, str(file_path), sample_headers)
    
    assert result == str(file_path)
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        assert rows == [sample_headers] + sample_data