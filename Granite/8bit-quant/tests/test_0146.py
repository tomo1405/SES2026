import csv
from ipaddress import IPv4Network
from src_0146 import task_func
import pytest

def test_task_func_valid_ip_range():
    ip_range = '192.168.1.0/24'
    csv_path = 'test_ip_range.csv'
    result = task_func(ip_range, csv_path)
    assert result == 'test_ip_range.csv'
    with open(csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ip_address = row['IP Address']
            assert IPv4Network(ip_range).contains(ip_address)

def test_task_func_invalid_ip_range():
    ip_range = '192.168.1'
    csv_path = 'test_ip_range.csv'
    with pytest.raises(ValueError):
        task_func(ip_range, csv_path)

def test_task_func_invalid_csv_path():
    ip_range = '192.168.1.0/24'
    csv_path = '/invalid/path/test_ip_range.csv'
    with pytest.raises(FileNotFoundError):
        task_func(ip_range, csv_path)