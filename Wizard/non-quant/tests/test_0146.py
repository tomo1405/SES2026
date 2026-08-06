python
import csv
from ipaddress import IPv4Network
import pytest

def task_func(ip_range, csv_path):
    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ['IP Address']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for ip in IPv4Network(ip_range):
            writer.writerow({'IP Address': str(ip)})

    return csv_path

def test_task_func():
    ip_range = '192.168.0.0/24'
    csv_path = 'test.csv'

    task_func(ip_range, csv_path)

    with open(csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = [row for row in reader]

    assert len(rows) == 256
    assert rows[0]['IP Address'] == '192.168.0.0'
    assert rows[-1]['IP Address'] == '192.168.0.255'

    import os
    os.remove(csv_path)