import pytest
from src_0593 import task_func
import os
import csv
from datetime import datetime

# Mocking datetime to control the output
class MockDateTime(datetime):
    @classmethod
    def now(cls):
        return datetime(2023, 1, 1, 12, 0, 0, 0)

@pytest.fixture
def mock_datetime(monkeypatch):
    monkeypatch.setattr(datetime, 'now', MockDateTime.now)

@pytest.fixture
def temp_output_dir(tmpdir):
    return tmpdir.mkdir("output")

def test_task_func(mock_datetime, temp_output_dir):
    hours = 2
    file_path = task_func(hours, str(temp_output_dir))

    assert os.path.exists(file_path)

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    # Check header
    assert rows[0] == ['Time', 'Temperature', 'Humidity', 'Pressure']

    # Check number of rows
    assert len(rows) == hours + 1  # +1 for header

    # Check timestamps and values
    for row in rows[1:]:
        timestamp, *values = row
        assert timestamp == '2023-01-01 12:00:00.000000'
        assert all(0 <= int(value) <= 100 for value in values)

def test_task_func_nonexistent_output_dir(mock_datetime):
    hours = 1
    output_dir = './nonexistent_dir'
    file_path = task_func(hours, output_dir)

    assert os.path.exists(output_dir)
    assert os.path.exists(file_path)

def test_task_func_default_output_dir(mock_datetime):
    hours = 1
    file_path = task_func(hours)

    assert os.path.exists('./output')
    assert os.path.exists(file_path)