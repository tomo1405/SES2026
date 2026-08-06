python
import re
import os
from collections import Counter
import pytest

def task_func(folder_path: str) -> dict:
    IP_REGEX = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    counter = Counter()
    for filename in os.listdir(folder_path):
        if filename.endswith('.log'):
            with open(os.path.join(folder_path, filename)) as file:
                content = file.read()
                ips = re.findall(IP_REGEX, content)
                counter.update(ips)
    return dict(counter)

def test_task_func():
    # Test case 1
    folder_path = 'test_folder'
    expected_result = {'192.168.1.1': 1, '192.168.1.2': 1, '192.168.1.3': 1}
    result = task_func(folder_path)
    assert result == expected_result

    # Test case 2
    folder_path = 'test_folder_2'
    expected_result = {'192.168.1.1': 1, '192.168.1.2': 1, '192.168.1.3': 1}
    result = task_func(folder_path)
    assert result == expected_result

    # Test case 3
    folder_path = 'test_folder_3'
    expected_result = {}
    result = task_func(folder_path)
    assert result == expected_result