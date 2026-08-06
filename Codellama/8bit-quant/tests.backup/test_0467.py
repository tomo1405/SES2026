import pytest
from src_0467 import task_func

class TestTaskFunc:
    def test_task_func_with_enum(self):
        my_obj = {
            "color": Color.RED
        }
        result = task_func(my_obj)
        assert result == '{"color": "RED"}'

    def test_task_func_with_non_enum(self):
        my_obj = {
            "name": "John Doe"
        }
        result = task_func(my_obj)
        assert result == '{"name": "John Doe"}'