import os
import time

from src_0264 import task_func


def test_task_func():
    # Test that the function returns the correct archive directory
    assert task_func('path/to/files', 30) == 'path/to/files/archive'

    # Test that the function moves files with the correct extensions
    assert os.path.isfile('path/to/files/archive/file.txt')
    assert os.path.isfile('path/to/files/archive/file.csv')
    assert os.path.isfile('path/to/files/archive/file.xlsx')
    assert os.path.isfile('path/to/files/archive/file.docx')
    assert os.path.isfile('path/to/files/archive/file.pdf')

    # Test that the function moves files that are older than the specified number of days
    assert os.path.getmtime('path/to/files/archive/file.txt') < time.time() - 30 * 86400
    assert os.path.getmtime('path/to/files/archive/file.csv') < time.time() - 30 * 86400
    assert os.path.getmtime('path/to/files/archive/file.xlsx') < time.time() - 30 * 86400
    assert os.path.getmtime('path/to/files/archive/file.docx') < time.time() - 30 * 86400
    assert os.path.getmtime('path/to/files/archive/file.pdf') < time.time() - 30 * 86400

    # Test that the function does not move files that are not older than the specified number of days
    assert not os.path.isfile('path/to/files/archive/file.txt')
    assert not os.path.isfile('path/to/files/archive/file.csv')
    assert not os.path.isfile('path/to/files/archive/file.xlsx')
    assert not os.path.isfile('path/to/files/archive/file.docx')
    assert not os.path.isfile('path/to/files/archive/file.pdf')