import json
from enum import Enum
from src_0467 import task_func

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

def test_task_func():
    my_obj = {"color": Color.RED}
    expected_output = '{"color": "RED"}'
    actual_output = task_func(my_obj)
    assert actual_output == expected_output, "Output does not match expected output"

test_task_func()