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
    my_obj = {
        'name': 'John',
        'age': 30,
        'date': datetime(2021, 1, 1),
        'decimal': Decimal('1.23')
    }
    expected_result = '{"name": "John", "age": 30, "date": "2021-01-01T00:00:00", "decimal": "1.23"}'
    assert task_func(my_obj) == expected_result