import pytest
from src_0465 import task_func
from datetime import datetime
from decimal import Decimal

def test_task_func_with_datetime():
    my_obj = {"timestamp": datetime(2023, 1, 1, 12, 0, 0)}
    expected_output = '{"timestamp": "2023-01-01T12:00:00"}'
    assert task_func(my_obj) == expected_output

def test_task_func_with_decimal():
    my_obj = {"amount": Decimal("123.45")}
    expected_output = '{"amount": "123.45"}'
    assert task_func(my_obj) == expected_output

def test_task_func_with_mixed_types():
    my_obj = {
        "timestamp": datetime(2023, 1, 1, 12, 0, 0),
        "amount": Decimal("123.45"),
        "name": "Test"
    }
    expected_output = '{"timestamp": "2023-01-01T12:00:00", "amount": "123.45", "name": "Test"}'
    assert task_func(my_obj) == expected_output

def test_task_func_with_no_special_types():
    my_obj = {"name": "Test", "number": 123}
    expected_output = '{"name": "Test", "number": 123}'
    assert task_func(my_obj) == expected_output

def test_task_func_with_empty_dict():
    my_obj = {}
    expected_output = '{}'
    assert task_func(my_obj) == expected_output

def test_task_func_with_none_value():
    my_obj = {"value": None}
    expected_output = '{"value": null}'
    assert task_func(my_obj) == expected_output