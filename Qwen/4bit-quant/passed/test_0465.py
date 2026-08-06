import pytest
from src_0465 import task_func
from datetime import datetime
from decimal import Decimal

def test_task_func_with_datetime():
    my_obj = {
        "timestamp": datetime(2023, 10, 1, 12, 30, 45),
        "value": 123.45
    }
    expected_output = '{"timestamp": "2023-10-01T12:30:45", "value": 123.45}'
    assert task_func(my_obj) == expected_output

def test_task_func_with_decimal():
    my_obj = {
        "price": Decimal('123.45'),
        "discount": 0.10
    }
    expected_output = '{"price": "123.45", "discount": 0.1}'
    assert task_func(my_obj) == expected_output

def test_task_func_with_mixed_types():
    my_obj = {
        "created_at": datetime(2023, 10, 1, 12, 30, 45),
        "amount": Decimal('123.45'),
        "is_active": True,
        "tags": ["tag1", "tag2"]
    }
    expected_output = (
        '{"created_at": "2023-10-01T12:30:45", '
        '"amount": "123.45", '
        '"is_active": true, '
        '"tags": ["tag1", "tag2"]}'
    )
    assert task_func(my_obj) == expected_output

def test_task_func_with_empty_dict():
    my_obj = {}
    expected_output = '{}'
    assert task_func(my_obj) == expected_output

def test_task_func_with_none_value():
    my_obj = {
        "name": None,
        "age": 30
    }
    expected_output = '{"name": null, "age": 30}'
    assert task_func(my_obj) == expected_output