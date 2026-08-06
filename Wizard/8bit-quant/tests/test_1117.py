python
import random
import statistics
import pytest

# Constants
AGE_RANGE = (22, 60)

def task_func(dict1):
    emp_ages = []
    
    for prefix, num_employees in dict1.items():
        if not prefix.startswith('EMP$$'):
            continue

        for _ in range(num_employees):
            age = random.randint(*AGE_RANGE)
            emp_ages.append(age)

    # If no employees in EMP$$ department
    if not emp_ages:
        return 0, 0, []
    
    mean_age = statistics.mean(emp_ages)
    median_age = statistics.median(emp_ages)
    mode_age = statistics.multimode(emp_ages)

    return mean_age, median_age, mode_age

# Test cases
def test_task_func_valid_input():
    # Test with valid input
    input_dict = {'EMP$$1': 5, 'EMP$$2': 3, 'EMP$$3': 2}
    expected_output = (35.0, 35.0, [35.0])
    assert task_func(input_dict) == expected_output

def test_task_func_empty_input():
    # Test with empty input
    input_dict = {}
    expected_output = (0, 0, [])
    assert task_func(input_dict) == expected_output

def test_task_func_invalid_input():
    # Test with invalid input
    input_dict = {'EMP$$1': 5, 'EMP$$2': 3, 'EMP$$3': 'a'}
    expected_output = (0, 0, [])
    assert task_func(input_dict) == expected_output

def test_task_func_no_emp_department():
    # Test with no employees in EMP$$ department
    input_dict = {'EMP$$1': 0, 'EMP$$2': 0, 'EMP$$3': 0}
    expected_output = (0, 0, [])
    assert task_func(input_dict) == expected_output

# Run tests
pytest.main(['-v'])