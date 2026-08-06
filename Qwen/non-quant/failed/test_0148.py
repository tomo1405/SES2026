import pytest
from src_0148 import task_func
from ipaddress import IPv4Address

def test_task_func_single_ip_open_port(mocker):
    # Mock the socket connection to always succeed
    mock_socket = mocker.patch('src_0148.socket.socket')
    mock_socket_instance = mock_socket.return_value
    mock_socket_instance.connect.return_value = None
    mock_socket_instance.settimeout.return_value = None

    ip_range = '192.168.1.1/32'
    port = 80

    result = task_func(ip_range, port)
    expected_result = {'192.168.1.1': True}

    assert result == expected_result

def test_task_func_single_ip_closed_port(mocker):
    # Mock the socket connection to always fail
    mock_socket = mocker.patch('src_0148.socket.socket')
    mock_socket_instance = mock_socket.return_value
    mock_socket_instance.connect.side_effect = socket.error
    mock_socket_instance.settimeout.return_value = None

    ip_range = '192.168.1.1/32'
    port = 80

    result = task_func(ip_range, port)
    expected_result = {'192.168.1.1': False}

    assert result == expected_result

def test_task_func_multiple_ips(mocker):
    # Mock the socket connection to succeed for one IP and fail for another
    mock_socket = mocker.patch('src_0148.socket.socket')
    mock_socket_instance = mock_socket.return_value
    mock_socket_instance.connect.side_effect = [None, socket.error]
    mock_socket_instance.settimeout.return_value = None

    ip_range = '192.168.1.1/31'
    port = 80

    result = task_func(ip_range, port)
    expected_result = {
        '192.168.1.1': True,
        '192.168.1.2': False
    }

    assert result == expected_result

def test_task_func_invalid_ip_range():
    ip_range = 'invalid_ip_range'
    port = 80

    with pytest.raises(ValueError):
        task_func(ip_range, port)

def test_task_func_invalid_port():
    ip_range = '192.168.1.1/32'
    port = -1

    with pytest.raises(OSError):
        task_func(ip_range, port)