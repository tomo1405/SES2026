import pytest
from src_0501 import task_func

# Test cases for the task_func function

def test_task_func():
    # Test case 1: Basic functionality
    values = [
        {'ID': 1, 'Name': 'Alice', 'Age': 30},
        {'ID': 2, 'Name': 'Bob', 'Age': 25}
    ]
    filename = 'test_output.xls'
    result = task_func(values, filename)
    assert os.path.exists(result), "File not created"
    os.remove(result)

    # Add more test cases as needed

if __name__ == "__main__":
    pytest.main()