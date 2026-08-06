import pytest
from src_0145 import task_func

def test_task_func_valid_ip_range():
    # Mocking the requests.get to simulate a successful response
    with pytest.raises(requests.exceptions.ConnectionError):
        task_func("192.168.1.0/30", 1)

def test_task_func_invalid_ip_range():
    with pytest.raises(ValueError, match="Invalid IP range"):
        task_func("256.256.256.256/30", 1)

def test_task_func_timeout():
    # Mocking the requests.get to simulate a timeout
    with pytest.raises(requests.exceptions.Timeout):
        task_func("192.168.1.0/30", 0.001)

def test_task_func_no_response():
    # Mocking the requests.get to simulate no response
    with pytest.raises(requests.exceptions.ConnectionError):
        task_func("192.168.1.0/30", 1)

def test_task_func_successful_response(mocker):
    # Mocking the requests.get to simulate a successful response
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mocker.patch('requests.get', return_value=mock_response)

    result = task_func("192.168.1.0/30", 1)
    assert result == ['192.168.1.0', '192.168.1.1', '192.168.1.2', '192.168.1.3']

def test_task_func_empty_range():
    result = task_func("0.0.0.0/32", 1)
    assert result == []

def test_task_func_large_range(mocker):
    # Mocking the requests.get to simulate a successful response
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mocker.patch('requests.get', return_value=mock_response)

    result = task_func("10.0.0.0/8", 1)
    assert len(result) == 254  # Only 254 IPs in the range (excluding 10.0.0.0 and 10.0.0.255)