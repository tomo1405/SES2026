import json
from datetime import datetime
from decimal import Decimal
from src_0465 import task_func
import pytest

def test_task_func():
    my_obj = {"key1": "value1", "key2": datetime.now(), "key3": Decimal("123.45")}
    expected_result = '{"key1": "value1", "key2": "2022-01-01T00:00:00", "key3": "123.45"}'
    result = task_func(my_obj)
    assert result == expected_result

def test_task_func_with_invalid_input():
    my_obj = {"key1": "value1", "key2": "invalid_datetime", "key3": "invalid_decimal"}
    with pytest.raises(TypeError):
        task_func(my_obj)