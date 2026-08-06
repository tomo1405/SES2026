python
import gzip
import difflib
import pytest

from src_0511 import task_func

def test_task_func():
    file1 = 'file1.txt.gz'
    file2 = 'file2.txt.gz'
    with gzip.open(file1, 'wt') as f1, gzip.open(file2, 'wt') as f2:
        f1.write('line1\nline2\nline3\n')
        f2.write('line1\nline3\nline4\n')

    result = task_func(file1, file2)
    expected = '+ line2\n- line4\n'

    assert result == expected

    with pytest.raises(FileNotFoundError):
        task_func('nonexistent_file.txt.gz', 'nonexistent_file2.txt.gz')