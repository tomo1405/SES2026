import os
import os.path
import csv
import collections
from unittest import mock

# Constants
FILE_NAME = 'file_sizes.csv'

def task_func(my_path):
    file_sizes = collections.defaultdict(int)

    for dirpath, dirnames, filenames in os.walk(my_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            file_sizes[f] += os.path.getsize(fp)

    with open(os.path.join(my_path, FILE_NAME), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['File Name', 'Size'])
        for row in file_sizes.items():
            writer.writerow(row)

    return os.path.join(my_path, FILE_NAME)

def test_task_func():
    with mock.patch('src_0267.os.walk') as mock_walk, \
         mock.patch('src_0267.os.path.getsize') as mock_getsize, \
         mock.patch('src_0267.csv.writer') as mock_writer:

        mock_walk.return_value = [('/path/to/my_path', [], ['file1.txt', 'file2.txt'])]
        mock_getsize.side_effect = [100, 200]

        task_func('/path/to/my_path')

        mock_writer.assert_called_with(mock.ANY)
        mock_writer.return_value.writerow.assert_has_calls([
            mock.call(['File Name', 'Size']),
            mock.call(('file1.txt', 100)),
            mock.call(('file2.txt', 200))
        ])