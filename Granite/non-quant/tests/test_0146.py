import csv
from ipaddress import IPv4Network
from unittest.mock import patch, mock_open, call

def task_func(ip_range, csv_path):
    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ['IP Address']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for ip in IPv4Network(ip_range):
            writer.writerow({'IP Address': str(ip)})

    return csv_path

def test_task_func():
    ip_range = '192.168.1.0/24'
    csv_path = 'output.csv'

    with patch('src_0146.open', mock_open()) as mock_file:
        task_func(ip_range, csv_path)

    mock_file.assert_has_calls([
        call(csv_path, 'w', newline=''),
        call().__enter__(),
        call().writeheader(),
        call().writerow({'IP Address': '192.168.1.1'}),
        call().writerow({'IP Address': '192.168.1.2'}),
        call().writerow({'IP Address': '192.168.1.3'}),
        call().__exit__(None, None, None),
    ])