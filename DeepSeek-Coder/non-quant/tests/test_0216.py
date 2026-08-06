import pytest
from src_0216 import task_func

def test_task_func():
    url = "https://api.example.com/data"
    parameters = {"param1": "value1"}
    result = task_func(url, parameters)
    assert result is not None