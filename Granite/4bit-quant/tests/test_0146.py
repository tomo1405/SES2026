import csv
from ipaddress import IPv4Network
from src_0146 import task_func
import pytest

def test_task_func():
    ip_range = '192.168.0.0/24'
    csv_path = 'test_ip_addresses.csv'
    expected_csv_path = 'expected_ip_addresses.csv'

    # Call the function and store the result
    result = task_func(ip_range, csv_path)

    # Check if the result is the expected CSV file path
    assert result == expected_csv_path

    # Check if the CSV file was created
    assert os.path.exists(csv_path)

    # Read the generated CSV file and check if it contains the expected IP addresses
    with open(csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        ip_addresses = [row['IP Address'] for row in reader]

    expected_ip_addresses = [str(ip) for ip in IPv4Network(ip_range)]
    assert ip_addresses == expected_ip_addresses

    # Clean up - delete the generated CSV file
    os.remove(csv_path)