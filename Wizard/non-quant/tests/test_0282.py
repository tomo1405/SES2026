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
    # Test case 1: Valid folder path
    folder_path = 'tests/test_data'
    expected_result = {'192.168.1.1': 2, '192.168.1.2': 1}
    assert task_func(folder_path) == expected_result

    # Test case 2: Invalid folder path
    folder_path = 'tests/invalid_folder'
    with pytest.raises(FileNotFoundError):
        task_func(folder_path)

    # Test case 3: Empty folder path
    folder_path = ''
    with pytest.raises(FileNotFoundError):
        task_func(folder_path)

    # Test case 4: Folder path with no log files
    folder_path = 'tests/test_data/no_log_files'
    expected_result = {}
    assert task_func(folder_path) == expected_result

    # Test case 5: Folder path with no log files and no other files
    folder_path = 'tests/test_data/no_files'
    expected_result = {}
    assert task_func(folder_path) == expected_result

    # Test case 6: Folder path with only log files
    folder_path = 'tests/test_data/only_log_files'
    expected_result = {'192.168.1.1': 2, '192.168.1.2': 1}
    assert task_func(folder_path) == expected_result

    # Test case 7: Folder path with only log files and no other files
    folder_path = 'tests/test_data/only_log_files_no_other_files'
    expected_result = {'192.168.1.1': 2, '192.168.1.2': 1}
    assert task_func(folder_path) == expected_result

    # Test case 8: Folder path with only other files
    folder_path = 'tests/test_data/only_other_files'
    expected_result = {}
    assert task_func(folder_path) == expected_result

    # Test case 9: Folder path with only other files and no log files
    folder_path = 'tests/test_data/only_other_files_no_log_files'
    expected_result = {}
    assert task_func(folder_path) == expected_result

    # Test case 10: Folder path with only log files and empty files
    folder_path = 'tests/test_data/empty_files'
    expected_result = {'192.168.1.1': 2, '192.168.1.2': 1}
    assert task_func(folder_path) == expected_result

    # Test case 11: Folder path with only log files and invalid files
    folder_path = 'tests/test_data/invalid_files'
    expected_result = {'192.168.1.1': 2, '192.168.1.2': 1}
    assert task_func(folder_path) == expected_result

    # Test case 12: Folder path with only log files and invalid IPs
    folder_path = 'tests/test_data/invalid_ips'
    expected_result = {'192.168.1.1': 2, '192.168.1.2': 1}
    assert task_func(folder_path) == expected_result