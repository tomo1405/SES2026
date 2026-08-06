import pytest
from src_0877 import task_func

def test_task_func():
    data_dict = {'a': 1, 'b': 2, 'c': 3}
    source_directory = 'source_dir'
    backup_directory = 'backup_dir'

    data_dict, sorted_dict, backup_status = task_func(data_dict, source_directory, backup_directory)

    assert data_dict == {'a': 1, 'b': 2, 'c': 3, 'a': 1}
    assert sorted_dict == [('a', 2), ('b', 1), ('c', 1)]
    assert backup_status == True