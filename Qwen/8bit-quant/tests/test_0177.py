import pytest
from src_0177 import task_func

def test_task_func_valid_ips():
    ip_addresses = ['8.8.8.8', '1.1.1.1']
    expected_output = {'8.8.8.8': 'dns.google', '1.1.1.1': 'one.one.one.one'}
    assert task_func(ip_addresses) == expected_output

def test_task_func_invalid_ips():
    ip_addresses = ['256.256.256.256', 'not-an-ip']
    expected_output = {'256.256.256.256': None, 'not-an-ip': None}
    assert task_func(ip_addresses) == expected_output

def test_task_func_mixed_ips():
    ip_addresses = ['8.8.8.8', 'not-an-ip', '1.1.1.1']
    expected_output = {'8.8.8.8': 'dns.google', 'not-an-ip': None, '1.1.1.1': 'one.one.one.one'}
    assert task_func(ip_addresses) == expected_output

def test_task_func_empty_list():
    ip_addresses = []
    expected_output = {}
    assert task_func(ip_addresses) == expected_output

def test_task_func_single_ip():
    ip_addresses = ['8.8.8.8']
    expected_output = {'8.8.8.8': 'dns.google'}
    assert task_func(ip_addresses) == expected_output

def test_task_func_no_resolvable_ip():
    ip_addresses = ['192.168.1.1']  # Assuming this IP is not resolvable
    expected_output = {'192.168.1.1': None}
    assert task_func(ip_addresses) == expected_output