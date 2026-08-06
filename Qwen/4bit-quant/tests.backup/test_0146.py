import pytest
from src_0146 import task_func
import os
from ipaddress import IPv4Network

def test_task_func_valid_ip_range(tmpdir):
    # Create a temporary CSV file path
    csv_path = tmpdir.join('test.csv').strpath
    
    # Define a valid IP range
    ip_range = '192.168.1.0/30'
    
    # Call the function
    result = task_func(ip_range, csv_path)
    
    # Check if the function returns the correct path
    assert result == csv_path
    
    # Check if the CSV file exists
    assert os.path.exists(csv_path)
    
    # Read the CSV file and check its contents
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        
        # Expected IP addresses in the range 192.168.1.0/30
        expected_ips = [str(ip) for ip in IPv4Network(ip_range)]
        
        # Check if the CSV contains the correct IP addresses
        assert len(rows) == len(expected_ips)
        for i, row in enumerate(rows):
            assert row['IP Address'] == expected_ips[i]

def test_task_func_invalid_ip_range(tmpdir):
    # Create a temporary CSV file path
    csv_path = tmpdir.join('test.csv').strpath
    
    # Define an invalid IP range
    ip_range = 'invalid_ip_range'
    
    # Call the function and expect it to raise a ValueError
    with pytest.raises(ValueError):
        task_func(ip_range, csv_path)

def test_task_func_empty_ip_range(tmpdir):
    # Create a temporary CSV file path
    csv_path = tmpdir.join('test.csv').strpath
    
    # Define an empty IP range
    ip_range = ''
    
    # Call the function and expect it to raise a ValueError
    with pytest.raises(ValueError):
        task_func(ip_range, csv_path)