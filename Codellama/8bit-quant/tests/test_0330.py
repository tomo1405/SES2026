import json

from src_0330 import task_func


def test_task_func():
    file_path = 'test_data.json'
    regex_pattern = r'\(.+?\)|\w'
    expected_output = {'test_data.json': ['hello', 'world']}

    with open(file_path, 'w') as file:
        json.dump({'key1': 'hello', 'key2': 'world'}, file)

    output = task_func(file_path, regex_pattern)

    assert output == expected_output