python
import collections
import operator
import os
import shutil
import pytest

def task_func(data_dict, source_directory, backup_directory):
    # Add the key 'a' with value 1
    data_dict.update({'a': 1})

    # Count the frequency of the values
    counter = collections.Counter(data_dict.values())

    # Sort the dictionary by the frequency
    sorted_dict = sorted(counter.items(), key=operator.itemgetter(1), reverse=True)

    # Backup files
    backup_status = False
    if os.path.isdir(source_directory):
        shutil.copytree(source_directory, backup_directory, dirs_exist_ok=True)
        backup_status = True

    return data_dict, sorted_dict, backup_status

def test_task_func():
    data_dict = {'a': 2, 'b': 3, 'c': 1}
    source_directory = 'source_directory'
    backup_directory = 'backup_directory'

    result = task_func(data_dict, source_directory, backup_directory)

    assert result[0] == {'a': 1, 'b': 3, 'c': 1}
    assert result[1] == [(1, 1), (3, 1)]
    assert result[2] == True