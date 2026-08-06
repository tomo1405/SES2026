import json

from src_0413 import task_func


def test_task_func():
    json_file = 'test_data.json'
    expected_result = {'key1': 'value1', 'key2': 'value2'}

    with open(json_file, 'w') as f:
        json.dump(expected_result, f)

    result = task_func(json_file)

    assert result == expected_result