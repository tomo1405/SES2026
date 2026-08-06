python
import os
import ctypes
from datetime import datetime
import pytz
import pytest

def task_func(filepath):
    metadata = dict()
    lib = ctypes.CDLL(filepath)

    file_stat = os.stat(filepath)

    creation_time = datetime.fromtimestamp(file_stat.st_ctime, pytz.UTC)
    
    modification_time = datetime.fromtimestamp(file_stat.st_mtime, pytz.UTC)

    file_size = file_stat.st_size
    metadata['Creation Time'] = creation_time
    metadata['Modification Time'] = modification_time
    metadata['Size'] = file_size
    
    return lib._name, metadata

def test_task_func():
    filepath = 'test.so'
    name, metadata = task_func(filepath)
    assert name == 'test'
    assert metadata['Creation Time'] == datetime(2021, 1, 1, 0, 0, tzinfo=pytz.UTC)
    assert metadata['Modification Time'] == datetime(2021, 1, 2, 0, 0, tzinfo=pytz.UTC)
    assert metadata['Size'] == 1000