import subprocess
from ipaddress import IPv4Network
def task_func(ip_range):
    active_ips = {}

    for ip in IPv4Network(ip_range):
        try:
            subprocess.check_output(f'ping -c 1 {ip}', shell=True)
            active_ips[str(ip)] = True
        except subprocess.CalledProcessError:
            active_ips[str(ip)] = False

    return active_ips
import pytest

def test_task_func():
    active_ips = task_func('192.168.1.0/24')
    assert '192.168.1.1' in active_ips
    assert active_ips['192.168.1.1'] == True
    assert '192.168.1.254' in active_ips
    assert active_ips['192.168.1.254'] == False