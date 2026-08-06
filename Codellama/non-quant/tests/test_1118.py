import json

from src_1118 import task_func


def test_task_func():
    department_data = {'EMP$$': 10, 'MAN$$': 5, 'DEV$$': 3, 'HR$$': 2}
    expected_level_data = {'EMP$$': ['Junior', 'Mid', 'Senior', 'Junior', 'Mid', 'Senior', 'Junior', 'Mid', 'Senior', 'Junior'], 'MAN$$': ['Junior', 'Mid', 'Senior'], 'DEV$$': ['Junior', 'Mid', 'Senior'], 'HR$$': ['Junior', 'Mid']}
    assert task_func(department_data) == json.dumps(expected_level_data)