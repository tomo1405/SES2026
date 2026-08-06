python
import pytest
from src_0330 import task_func

def test_task_func():
    file_path = 'data.json'
    regex_pattern = r'\(.+?\)|\w'
    expected_result = {'data.json': ['(123)', 'abc']}

    with open(file_path, 'w') as file:
        json.dump({'key1': '(123)', 'key2': 'abc'}, file)

    result = task_func(file_path, regex_pattern)

    assert result == expected_result

    os.remove(file_path)