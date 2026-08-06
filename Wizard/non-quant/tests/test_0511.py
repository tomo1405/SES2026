python
import gzip
import difflib
import pytest

from src_0511 import task_func

def test_task_func():
    file1_content = ['line1\n', 'line2\n', 'line3\n']
    file2_content = ['line1\n', 'line2\n', 'line4\n']
    with gzip.open('file1.gz', 'wt') as file1, gzip.open('file2.gz', 'wt') as file2:
        file1.writelines(file1_content)
        file2.writelines(file2_content)

    result = task_func('file1.gz', 'file2.gz')
    expected = '+ line3\n- line4\n'

    assert result == expected