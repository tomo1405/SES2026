import json
from datetime import datetime
from decimal import Decimal
from src_0465 import task_func
import pytest

class TestTaskFunc:
    def test_task_func_with_datetime_object(self):
        my_obj = {"date": datetime.now()}
        expected_result = json.dumps({"date": my_obj["date"].isoformat()})
        assert task_func(my_obj) == expected_result

    def test_task_func_with_decimal_object(self):
        my_obj = {"amount": Decimal("10.5")}
        expected_result = json.dumps({"amount": str(my_obj["amount"])})
        assert task_func(my_obj) == expected_result

    def test_task_func_with_nested_objects(self):
        my_obj = {
            "date": datetime.now(),
            "amount": Decimal("10.5"),
            "nested": {"key": "value"},
        }
        expected_result = json.dumps(
            {
                "date": my_obj["date"].isoformat(),
                "amount": str(my_obj["amount"]),
                "nested": my_obj["nested"],
            }
        )
        assert task_func(my_obj) == expected_result

    def test_task_func_with_invalid_object(self):
        my_obj = {"file": open(__file__)}
        with pytest.raises(TypeError):
            task_func(my_obj)