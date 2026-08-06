python
import json
import pytest
from datetime import datetime
import numpy as np
from decimal import Decimal
from src_0466 import task_func

class TestTaskFunc:
    def test_json_dumps(self):
        my_obj = {'a': 1, 'b': '2', 'c': datetime.now(), 'd': np.array([1, 2, 3]), 'e': Decimal('1.23')}
        result = task_func(my_obj)
        assert isinstance(result, str)
        assert json.loads(result) == my_obj

    def test_json_dumps_invalid_type(self):
        my_obj = {'a': 1, 'b': '2', 'c': datetime.now(), 'd': np.array([1, 2, 3]), 'e': Decimal('1.23')}
        my_obj['f'] = set()
        with pytest.raises(TypeError):
            task_func(my_obj)