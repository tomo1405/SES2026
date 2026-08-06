import hashlib

from src_0272 import task_func


def test_task_func_returns_dict():
    data_dict = {'a': 1, 'b': 2, 'c': 3}
    result = task_func(data_dict)
    assert isinstance(result, dict)

def test_task_func_adds_key_a():
    data_dict = {'a': 1, 'b': 2, 'c': 3}
    result = task_func(data_dict)
    assert 'a' in result
    assert result['a'] == 1

def test_task_func_generates_random_salt():
    data_dict = {'a': 1, 'b': 2, 'c': 3}
    result = task_func(data_dict)
    assert 'salt' in result
    assert len(result['salt']) == 5

def test_task_func_concatenates_values_with_salt():
    data_dict = {'a': 1, 'b': 2, 'c': 3}
    result = task_func(data_dict)
    assert 'a' in result
    assert 'b' in result
    assert 'c' in result
    assert result['a'] == hashlib.sha256((str(1) + result['salt']).encode()).hexdigest()
    assert result['b'] == hashlib.sha256((str(2) + result['salt']).encode()).hexdigest()
    assert result['c'] == hashlib.sha256((str(3) + result['salt']).encode()).hexdigest()

def test_task_func_adds_timestamp():
    data_dict = {'a': 1, 'b': 2, 'c': 3}
    result = task_func(data_dict)
    assert 'timestamp' in result
    assert isinstance(result['timestamp'], float)