import json
import math
from src_0255 import task_func

def test_task_func():
    assert task_func(16) == '4.0'
    assert task_func(25) == '5.0'
    assert task_func(36) == '6.0'
    assert task_func(49) == '7.0'
    assert task_func(64) == '8.0'

def test_task_func_with_precision():
    assert task_func(16, 1) == '4.0'
    assert task_func(25, 1) == '5.0'
    assert task_func(36, 1) == '6.0'
    assert task_func(49, 1) == '7.0'
    assert task_func(64, 1) == '8.0'

def test_task_func_with_negative_value():
    assert task_func(-16) == 'nan'
    assert task_func(-25) == 'nan'
    assert task_func(-36) == 'nan'
    assert task_func(-49) == 'nan'
    assert task_func(-64) == 'nan'

def test_task_func_with_string_input():
    assert task_func('abc') == 'nan'
    assert task_func('123') == 'nan'
    assert task_func('xyz') == 'nan'

def test_task_func_with_invalid_precision():
    assert task_func(16, 'abc') == 'nan'
    assert task_func(25, 'def') == 'nan'
    assert task_func(36, 'ghi') == 'nan'
    assert task_func(49, 'jkl') == 'nan'
    assert task_func(64, 'mno') == 'nan'