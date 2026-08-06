import time

import pytest
from src_0272 import task_func


def test_task_func_with_default_seed():
    input_data = {'b': 2}
    expected_output = {
        'a': 'd1fe173d8e9c8c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e',
        'b': 'd1fe173d8e9c8c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e',
        'timestamp': pytest.approx(time.time(), abs=1)
    }
    result = task_func(input_data)
    assert result['a'] == expected_output['a']
    assert result['b'] == expected_output['b']
    assert result['timestamp'] == pytest.approx(expected_output['timestamp'], abs=1)

def test_task_func_with_custom_seed():
    input_data = {'c': 3}
    expected_output = {
        'a': 'd1fe173d8e9c8c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e',
        'c': 'd1fe173d8e9c8c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e',
        'timestamp': pytest.approx(time.time(), abs=1)
    }
    result = task_func(input_data, seed=42)
    assert result['a'] == expected_output['a']
    assert result['c'] == expected_output['c']
    assert result['timestamp'] == pytest.approx(expected_output['timestamp'], abs=1)

def test_task_func_with_empty_dict():
    input_data = {}
    expected_output = {
        'a': 'd1fe173d8e9c8c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e',
        'timestamp': pytest.approx(time.time(), abs=1)
    }
    result = task_func(input_data)
    assert result['a'] == expected_output['a']
    assert result['timestamp'] == pytest.approx(expected_output['timestamp'], abs=1)

def test_task_func_with_multiple_keys():
    input_data = {'d': 4, 'e': 5}
    expected_output = {
        'a': 'd1fe173d8e9c8c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e',
        'd': 'd1fe173d8e9c8c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e',
        'e': 'd1fe173d8e9c8c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e9c8e',
        'timestamp': pytest.approx(time.time(), abs=1)
    }
    result = task_func(input_data)
    assert result['a'] == expected_output['a']
    assert result['d'] == expected_output['d']
    assert result['e'] == expected_output['e']
    assert result['timestamp'] == pytest.approx(expected_output['timestamp'], abs=1)