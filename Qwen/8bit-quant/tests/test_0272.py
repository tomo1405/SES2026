import pytest
from src_0272 import task_func
import hashlib
import time

def test_task_func_basic():
    input_data = {'b': 2}
    expected_output = {
        'a': hashlib.sha256('1'.encode()).hexdigest(),
        'b': hashlib.sha256('2'.encode()).hexdigest(),
        'timestamp': pytest.approx(time.time(), abs=1)
    }
    result = task_func(input_data)
    assert 'a' in result
    assert 'b' in result
    assert 'timestamp' in result
    assert result['a'] == expected_output['a']
    assert result['b'] == expected_output['b']
    assert result['timestamp'] == expected_output['timestamp']

def test_task_func_with_salt():
    input_data = {'c': 3}
    expected_output = {
        'a': hashlib.sha256('1'.encode()).hexdigest(),
        'c': hashlib.sha256('3'.encode()).hexdigest(),
        'timestamp': pytest.approx(time.time(), abs=1)
    }
    result = task_func(input_data, seed=42)
    assert 'a' in result
    assert 'c' in result
    assert 'timestamp' in result
    assert result['a'] == expected_output['a']
    assert result['c'] == expected_output['c']
    assert result['timestamp'] == expected_output['timestamp']

def test_task_func_empty_input():
    input_data = {}
    expected_output = {
        'a': hashlib.sha256('1'.encode()).hexdigest(),
        'timestamp': pytest.approx(time.time(), abs=1)
    }
    result = task_func(input_data)
    assert 'a' in result
    assert 'timestamp' in result
    assert result['a'] == expected_output['a']
    assert result['timestamp'] == expected_output['timestamp']

def test_task_func_multiple_keys():
    input_data = {'d': 4, 'e': 5}
    expected_output = {
        'a': hashlib.sha256('1'.encode()).hexdigest(),
        'd': hashlib.sha256('4'.encode()).hexdigest(),
        'e': hashlib.sha256('5'.encode()).hexdigest(),
        'timestamp': pytest.approx(time.time(), abs=1)
    }
    result = task_func(input_data)
    assert 'a' in result
    assert 'd' in result
    assert 'e' in result
    assert 'timestamp' in result
    assert result['a'] == expected_output['a']
    assert result['d'] == expected_output['d']
    assert result['e'] == expected_output['e']
    assert result['timestamp'] == expected_output['timestamp']