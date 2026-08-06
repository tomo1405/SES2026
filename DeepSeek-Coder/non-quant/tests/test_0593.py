import pytest
from src_0593 import task_func

def test_task_func():
    # Test the function with a specific number of hours
    hours = 2
    result = task_func(hours)
    assert os.path.exists(result), "The file was not created"
    assert os.path.isfile(result), "The file does not exist"

    # Additional assertions to verify the content of the file
    with open(result, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        assert len(data) == hours + 1, "The number of rows is incorrect"
        assert len(data[0]) == len(SENSORS) + 1, "The number of columns is incorrect"
        assert data[0] == ['Time'] + SENSORS, "The header is incorrect"