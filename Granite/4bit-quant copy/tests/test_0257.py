import json
import random
import hashlib
from datetime import datetime
from src_0257 import task_func
import pytest

def test_task_func():
    utc_datetime = datetime.now()
    salt = 'salt'
    password_length = 10
    seed = 0
    random.seed(seed)
    password = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(password_length))
    salted_string = utc_datetime.strftime("%Y-%m-%d %H:%M:%S") + salt
    hashed_password = hashlib.sha256((password + salted_string).encode('utf-8')).hexdigest()
    password_json_str = json.dumps(hashed_password)
    result = task_func(utc_datetime, salt, password_length, seed)
    assert result == password_json_str

def test_task_func_invalid_datetime():
    with pytest.raises(ValueError):
        task_func('invalid_datetime', 'salt', 10, 0)

def test_task_func_invalid_salt():
    with pytest.raises(ValueError):
        task_func(datetime.now(), 123, 10, 0)

def test_task_func_invalid_password_length():
    with pytest.raises(ValueError):
        task_func(datetime.now(), 'salt', 'invalid_password_length', 0)

def test_task_func_invalid_seed():
    with pytest.raises(ValueError):
        task_func(datetime.now(), 'salt', 10, 'invalid_seed')