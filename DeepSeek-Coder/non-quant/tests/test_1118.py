import pytest
from src_1118 import task_func

# Test cases
def test_task_func():
    # Test case 1: Basic functionality
    department_data = {
        'EMP$$': 3,
        'MAN$$': 2,
        'DEV$$': 4,
        'HR$$': 1
    }
    expected_output = '{"EMP$$": ["Junior", "Junior", "Junior", "Mid", "Mid", "Senior", "Senior", "Senior", "Senior"], "MAN$$": ["Junior", "Junior"], "DEV$$": ["Junior", "Junior", "Junior", "Junior"], "HR$$": ["Junior"]}'
    assert task_func(department_data) == expected_output

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()