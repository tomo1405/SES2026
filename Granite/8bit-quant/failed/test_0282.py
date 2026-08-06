import re
import os
from collections import Counter
from unittest.mock import patch, mock_open, MagicMock

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
    with patch('src_0282.os.listdir') as mock_listdir, \
         patch('src_0282.open', new_callable=mock_open), \
         patch('src_0282.re.findall') as mock_findall:
        # Test case 1: No files in folder
        mock_listdir.return_value = []
        result = task_func('folder_path')
        assert result == {}

        # Test case 2: One file with one IP address
        mock_listdir.return_value = ['file1.log']
        mock_file = mock_open()
        mock_file.read.return_value = '192.168.1.1'
        with patch('src_0282.open', mock_file):
            mock_findall.return_value = ['192.168.1.1']
            result = task_func('folder_path')
            assert result == {'192.168.1.1': 1}

        # Test case 3: Two files with two IP addresses
        mock_listdir.return_value = ['file1.log', 'file2.log']
        mock_file1 = mock_open()
        mock_file1.read.return_value = '192.168.1.1\n192.168.1.2'
        mock_file2 = mock_open()
        mock_file2.read.return_value = '192.168.1.3\n192.168.1.4'
        with patch('src_0282.open', side_effect=[mock_file1, mock_file2]):
            mock_findall.side_effect = [['192.168.1.1', '192.168.1.2'], ['192.168.1.3', '192.168.1.4']]
            result = task_func('folder_path')
            assert result == {'192.168.1.1': 1, '192.168.1.2': 1, '192.168.1.3': 1, '192.168.1.4': 1}