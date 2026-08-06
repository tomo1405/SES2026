import pytest
from src_0146 import task_func
from ipaddress import IPv4Network
import os

def test_task_func_valid_ip_range(tmpdir):
    ip_range = '192.168.1.0/30'
    csv_path = str(tmpdir.join('test_output.csv'))
    result = task_func(ip_range, csv_path)
    
    assert result == csv_path
    assert os.path.exists(csv_path)
    
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
    
    expected_ips = [str(ip) for ip in IPv4Network(ip_range)]
    actual_ips = [row['IP Address'] for row in rows]
    
    assert actual_ips == expected_ips

def test_task_func_invalid_ip_range(tmpdir):
    ip_range = '256.256.256.256/30'
    csv_path = str(tmpdir.join('test_output.csv'))
    
    with pytest.raises(ValueError):
        task_func(ip_range, csv_path)

def test_task_func_empty_ip_range(tmpdir):
    ip_range = '192.168.1.0/32'  # This will only generate one IP address
    csv_path = str(tmpdir.join('test_output.csv'))
    result = task_func(ip_range, csv_path)
    
    assert result == csv_path
    assert os.path.exists(csv_path)
    
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
    
    expected_ips = [str(ip) for ip in IPv4Network(ip_range)]
    actual_ips = [row['IP Address'] for row in rows]
    
    assert actual_ips == expected_ips

def test_task_func_existing_file(tmpdir):
    ip_range = '192.168.1.0/30'
    csv_path = str(tmpdir.join('test_output.csv'))
    
    # Create an existing file
    with open(csv_path, 'w') as f:
        pass
    
    result = task_func(ip_range, csv_path)
    
    assert result == csv_path
    assert os.path.exists(csv_path)
    
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
    
    expected_ips = [str(ip) for ip in IPv4Network(ip_range)]
    actual_ips = [row['IP Address'] for row in rows]
    
    assert actual_ips == expected_ips