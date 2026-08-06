python
import json
from datetime import datetime
from decimal import Decimal
import pytest

def task_func(my_obj):
    class DateTimeEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            if isinstance(obj, Decimal):
                return str(obj)
            return json.JSONEncoder.default(self, obj)
    return json.dumps(my_obj, cls=DateTimeEncoder)

def test_task_func():
    my_obj = {'a': 1, 'b': '2', 'c': datetime.now(), 'd': Decimal('3.14')}
    expected_result = '{"a": 1, "b": "2", "c": "2021-10-12T13:55:30.123456", "d": "3.14"}'
    assert task_func(my_obj) == expected_result