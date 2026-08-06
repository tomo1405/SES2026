import pytest
from src_0146 import task_func
from ipaddress import IPv4Network
import os

def test_task_func_valid_ip_range(tmpdir):
    ip_range = "192.168.1.0/30"
    csv_path = str(tmpdir / "test_output.csv")
    result = task_func(ip_range, csv_path)
    
    assert result == csv_path
    assert os.path.exists(csv_path)
    
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        ip_addresses = [row['IP Address'] for row in reader]
    
    expected_ips = ['192.168.1.0', '192.168.1.1', '192.168.1.2', '192.168.1.3']
    assert ip_addresses == expected_ips

def test_task_func_invalid_ip_range(tmpdir):
    ip_range = "invalid_ip_range"
    csv_path = str(tmpdir / "test_output.csv")
    
    with pytest.raises(ValueError):
        task_func(ip_range, csv_path)

def test_task_func_empty_ip_range(tmpdir):
    ip_range = "192.168.1.0/32"
    csv_path = str(tmpdir / "test_output.csv")
    result = task_func(ip_range, csv_path)
    
    assert result == csv_path
    assert os.path.exists(csv_path)
    
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        ip_addresses = [row['IP Address'] for row in reader]
    
    expected_ips = ['192.168.1.0']
    assert ip_addresses == expected_ips