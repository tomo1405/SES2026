import pytest
from src_0272 import task_func

def test_task_func_with_default_seed():
    input_data = {'b': 2, 'c': 3}
    expected_output = {
        'a': '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08',
        'b': '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08',
        'c': '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08',
        'timestamp': pytest.approx(time.time(), abs=1)
    }
    result = task_func(input_data, seed=0)
    assert result == expected_output

def test_task_func_with_custom_seed():
    input_data = {'x': 10, 'y': 20}
    expected_output = {
        'a': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
        'x': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
        'y': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
        'timestamp': pytest.approx(time.time(), abs=1)
    }
    result = task_func(input_data, seed=42)
    assert result == expected_output

def test_task_func_with_empty_input():
    input_data = {}
    expected_output = {
        'a': '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08',
        'timestamp': pytest.approx(time.time(), abs=1)
    }
    result = task_func(input_data, seed=0)
    assert result == expected_output

def test_task_func_with_non_string_values():
    input_data = {'z': 123, 'w': 456}
    expected_output = {
        'a': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
        'z': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
        'w': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
        'timestamp': pytest.approx(time.time(), abs=1)
    }
    result = task_func(input_data, seed=0)
    assert result == expected_output