import json
from datetime import datetime
import numpy as np
from decimal import Decimal
from src_0466 import task_func

def test_task_func_with_datetime():
    my_obj = {"date": datetime.now()}
    expected_result = json.dumps({"date": my_obj["date"].isoformat()})
    result = task_func(my_obj)
    assert result == expected_result

def test_task_func_with_numpy_array():
    my_obj = {"array": np.array([1, 2, 3])}
    expected_result = json.dumps({"array": my_obj["array"].tolist()})
    result = task_func(my_obj)
    assert result == expected_result

def test_task_func_with_decimal():
    my_obj = {"decimal": Decimal("1.2345678901234567890")}
    expected_result = json.dumps({"decimal": str(my_obj["decimal"])})
    result = task_func(my_obj)
    assert result == expected_result

def test_task_func_with_custom_object():
    class CustomObject:
        def __init__(self, value):
            self.value = value
    my_obj = {"custom_object": CustomObject("test")}
    expected_result = json.dumps({"custom_object": {"value": "test"}})
    result = task_func(my_obj)
    assert result == expected_result