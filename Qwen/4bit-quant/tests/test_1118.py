import json
import random

from src_1118 import task_func


# Mocking random.choice to control the output
class MockRandom:
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = 0

    def choice(self, seq):
        result = self.sequence[self.index % len(self.sequence)]
        self.index += 1
        return result

def test_task_func():
    # Mocking the random.choice to always return 'Junior'
    random.choice = MockRandom(['Junior'])

    # Test case data
    department_data = {
        'EMP$$': 3,
        'MAN$$': 2,
        'DEV$$': 1,
        'HR$$': 0,
        'INVALID$$': 5  # This should be ignored
    }

    # Expected result
    expected_result = {
        'EMP$$': ['Junior', 'Junior', 'Junior'],
        'MAN$$': ['Junior', 'Junior'],
        'DEV$$': ['Junior'],
        'HR$$': []
    }

    # Call the function
    result = task_func(department_data)

    # Convert result to dictionary for comparison
    result_dict = json.loads(result)

    # Assert the result
    assert result_dict == expected_result

def test_task_func_no_valid_prefixes():
    # Mocking the random.choice to always return 'Junior'
    random.choice = MockRandom(['Junior'])

    # Test case data with no valid prefixes
    department_data = {
        'INVALID$$': 5
    }

    # Expected result is an empty dictionary
    expected_result = {}

    # Call the function
    result = task_func(department_data)

    # Convert result to dictionary for comparison
    result_dict = json.loads(result)

    # Assert the result
    assert result_dict == expected_result

def test_task_func_zero_employees():
    # Mocking the random.choice to always return 'Junior'
    random.choice = MockRandom(['Junior'])

    # Test case data with zero employees
    department_data = {
        'EMP$$': 0,
        'MAN$$': 0,
        'DEV$$': 0,
        'HR$$': 0
    }

    # Expected result is an empty dictionary
    expected_result = {}

    # Call the function
    result = task_func(department_data)

    # Convert result to dictionary for comparison
    result_dict = json.loads(result)

    # Assert the result
    assert result_dict == expected_result