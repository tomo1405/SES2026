python
import json
import datetime
import numpy as np
import decimal
import pytest

from src_0466 import task_func

def test_task_func():
    my_obj = {
        'a': 1,
        'b': '2',
        'c': datetime.datetime.now(),
        'd': np.array([1, 2, 3]),
        'e': decimal.Decimal('3.14')
    }
    expected_result = '{"a": 1, "b": "2", "c": "' + my_obj['c'].isoformat() + '", "d": [1, 2, 3], "e": "3.14"}'
    assert task_func(my_obj) == expected_result