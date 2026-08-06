python
import collections
import random
import json

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

# Test cases
def test_task_func():
    department_data = {'EMP$$': 10, 'MAN$$': 5, 'DEV$$': 2, 'HR$$': 3}
    expected_output = '{"EMP$$": ["Junior", "Junior", "Junior", "Junior", "Junior", "Junior", "Junior", "Junior", "Junior", "Junior"], "MAN$$": ["Mid", "Mid", "Mid", "Mid", "Mid"], "DEV$$": ["Senior", "Senior"], "HR$$": ["Junior", "Junior", "Junior"]} '
    assert task_func(department_data) == expected_output

test_task_func()