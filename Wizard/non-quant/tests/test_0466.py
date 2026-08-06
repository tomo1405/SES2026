python
import json
import pytest
from src_0466 import task_func

class TestTaskFunc:
    def test_json_dumps(self):
        my_obj = {'a': 1, 'b': '2', 'c': [3, 4, 5], 'd': {'e': 6, 'f': '7'}, 'g': datetime.now()}
        result = task_func(my_obj)
        assert isinstance(result, str)
        assert json.loads(result) == my_obj

    def test_numpy_array(self):
        my_obj = {'a': 1, 'b': '2', 'c': np.array([3, 4, 5]), 'd': {'e': 6, 'f': '7'}, 'g': datetime.now()}
        result = task_func(my_obj)
        assert isinstance(result, str)
        assert json.loads(result) == {'a': 1, 'b': '2', 'c': [3, 4, 5], 'd': {'e': 6, 'f': '7'}, 'g': my_obj['g'].isoformat()}

    def test_decimal(self):
        my_obj = {'a': 1, 'b': '2', 'c': Decimal('3.14'), 'd': {'e': 6, 'f': '7'}, 'g': datetime.now()}
        result = task_func(my_obj)
        assert isinstance(result, str)
        assert json.loads(result) == {'a': 1, 'b': '2', 'c': '3.14', 'd': {'e': 6, 'f': '7'}, 'g': my_obj['g'].isoformat()}