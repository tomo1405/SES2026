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
    csv_path = 'ip_addresses.csv'

    result = task_func(ip_range, csv_path)

    assert result == csv_path
    assert isinstance(result, str)

    with open(csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            assert row['IP Address'] in IPv4Network(ip_range)

    import os
    os.remove(csv_path)