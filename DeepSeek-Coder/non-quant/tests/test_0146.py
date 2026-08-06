import pytest
from src_0146 import task_func
import csv
from ipaddress import IPv4Network
import io

def test_task_func():
    # Create a mock CSV content
    csv_content = io.StringIO()
    writer = csv.DictWriter(csv_content, fieldnames=['IP Address'])
    writer.writeheader()
    
    # Assuming the function is called with a valid IP range
    result = task_func('192.168.1.0/24', 'output.csv')
    
    # Read the generated CSV content
    csv_content.seek(0)
    reader = csv.DictReader(csv_content)
    rows = list(reader)
    
    # Assert the output
    assert len(rows) == 256  # 256 IPs in a /24 network
    assert rows[0]['IP Address'] == '192.168.1.0'
    assert result == 'output.csv'