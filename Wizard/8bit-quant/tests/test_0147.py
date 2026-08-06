python
import subprocess
from ipaddress import IPv4Network
import pytest

def task_func(ip_range):
    active_ips = {}

    for ip in IPv4Network(ip_range):
        try:
            subprocess.check_output(f'ping -c 1 {ip}', shell=True)
            active_ips[str(ip)] = True
        except subprocess.CalledProcessError:
            active_ips[str(ip)] = False

    return active_ips

def test_task_func():
    active_ips = task_func('192.168.0.0/24')
    assert active_ips == {'192.168.0.1': True, '192.168.0.2': True, '192.168.0.3': True, '192.168.0.4': True}

    active_ips = task_func('192.168.0.0/30')
    assert active_ips == {'192.168.0.1': True, '192.168.0.2': True}

    active_ips = task_func('192.168.0.0/31')
    assert active_ips == {'192.168.0.0': True, '192.168.0.1': True}

    active_ips = task_func('192.168.0.0/32')
    assert active_ips == {'192.168.0.0': True}

    active_ips = task_func('192.168.0.1')
    assert active_ips == {'192.168.0.1': True}

    active_ips = task_func('192.168.0.254')
    assert active_ips == {'192.168.0.254': True}

    active_ips = task_func('192.168.0.255')
    assert active_ips == {'192.168.0.255': True}

    active_ips = task_func('192.168.1.0/24')
    assert active_ips == {}

    active_ips = task_func('192.168.1.0/30')
    assert active_ips == {}

    active_ips = task_func('192.168.1.0/31')
    assert active_ips == {}

    active_ips = task_func('192.168.1.0/32')
    assert active_ips == {}

    active_ips = task_func('192.168.1.1')
    assert active_ips == {}

    active_ips = task_func('192.168.1.254')
    assert active_ips == {}

    active_ips = task_func('192.168.1.255')
    assert active_ips == {}