python
import collections
import random
import json
import pytest

# Constants
PREFICES = ['EMP$$', 'MAN$$', 'DEV$$', 'HR$$']
LEVELS = ['Junior', 'Mid', 'Senior']

def task_func(department_data):
    level_data = collections.defaultdict(list)
    
    for prefix, num_employees in department_data.items():
        if prefix not in PREFICES:
            continue

        for _ in range(num_employees):
            level = random.choice(LEVELS)
            level_data[prefix].append(level)

    return json.dumps(level_data)

def test_task_func():
    # Test case 1
    department_data = {'EMP$$': 10, 'MAN$$': 20, 'DEV$$': 30, 'HR$$': 40}
    expected_output = '{"EMP$$": ["Junior", "Mid", "Senior", "Junior", "Mid", "Senior", "Junior", "Mid", "Senior", "Junior", "Mid", "Senior"], "MAN$$": ["Junior", "Mid", "Senior", "Junior", "Mid", "Senior", "Junior", "Mid", "Senior", "Junior", "Mid", "Senior"], "DEV$$": ["Junior", "Mid", "Senior", "Junior", "Mid", "Senior", "Junior", "Mid", "Senior", "Junior", "Mid", "Senior"], "HR$$": ["Junior", "Mid", "Senior", "Junior", "Mid", "Senior", "Junior", "Mid", "Senior", "Junior", "Mid", "Senior"]}'
    assert task_func(department_data) == expected_output

    # Test case 2
    department_data = {'EMP$$': 0, 'MAN$$': 0, 'DEV$$': 0, 'HR$$': 0}
    expected_output = '{"EMP$$": [], "MAN$$": [], "DEV$$": [], "HR$$": []}'
    assert task_func(department_data) == expected_output

    # Test case 3
    department_data = {'EMP$$': 10, 'MAN$$': 20, 'DEV$$': 30, 'HR$$': 40, 'FOO$$': 50}
    expected_output = '{"EMP$$": ["Junior", "Mid", "Senior", "Junior", "Mid", "Senior", "Junior", "Mid", "Senior", "Junior", "Mid", "Senior"], "MAN$$": ["Junior", "Mid", "Senior", "Junior", "Mid", "Senior", "Junior", "Mid", "Senior", "Junior", "Mid", "Senior"], "DEV$$": ["Junior", "Mid", "Senior", "Junior", "Mid", "Senior", "Junior", "Mid", "Senior", "Junior", "Mid", "Senior"], "HR$$": ["Junior", "Mid", "Senior", "Junior", "Mid", "Senior", "Junior", "Mid", "Senior", "Junior", "Mid", "Senior"]}'
    assert task_func(department_data) == expected_output

    # Test case 4
    department_data = {'EMP$$': 10, 'MAN$$': 20, 'DEV$$': 30, 'HR$$': 40, 'FOO$$': 50}
    expected_output = '{"EMP$$": ["Junior", "Mid", "Senior", "Junior", "Mid", "Senior", "Junior", "Mid", "Senior", "Junior", "Mid", "Senior"], "MAN$$": ["Junior", "Mid", "Senior", "Junior", "Mid", "Senior", "Junior", "Mid", "Senior", "Junior", "Mid", "Senior"], "DEV$$": ["Junior", "Mid", "Senior", "Junior", "Mid", "Senior", "Junior", "Mid", "Senior", "Junior", "Mid", "Senior"], "HR$$": ["Junior", "Mid", "Senior", "Junior", "Mid", "Senior", "Junior", "Mid", "Senior", "Junior", "Mid", "Senior"], "FOO$$": []}'
    assert task_func(department_data) == expected_output