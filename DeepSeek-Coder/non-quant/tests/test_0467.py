import pytest
from src_0467 import task_func
import json
from enum import Enum

def test_task_func():
    class MyEnum(Enum):
        A = 1
        B = 2
    
    # Test with a simple object
    obj = {"key": "value"}
    result = task_func(obj)
    assert result == json.dumps({"key": "value"}, cls=EnumEncoder)

    # Add more test cases as needed