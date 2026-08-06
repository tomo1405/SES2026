import gzip

from src_0511 import task_func


def test_task_func():
    file_path1 = 'file1.txt.gz'
    file_path2 = 'file2.txt.gz'
    expected_diff = '+ line 1\n- line 2\n+ line 3\n- line 4\n'

    with gzip.open(file_path1, 'wt') as file1, gzip.open(file_path2, 'wt') as file2:
        file1.write('line 1\nline 2\nline 3\n')
        file2.write('line 1\nline 4\nline 3\n')

    diff = task_func(file_path1, file_path2)

    assert diff == expected_diff