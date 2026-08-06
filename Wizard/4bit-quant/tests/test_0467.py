python
import json
from enum import Enum
from src_0467 import task_func

class TestTaskFunc:
    def test_task_func(self):
        class Color(Enum):
            RED = 1
            GREEN = 2
            BLUE = 3
        my_obj = {'color': Color.RED, 'value': 100}
        expected_result = '{"color": "RED", "value": 100}'
        assert task_func(my_obj) == expected_result