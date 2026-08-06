import pytest
from src_1091 import task_func

def test_task_func():
    with open("test_data.json", "r") as f:
        data = json.load(f)

    key_frequency_counter = task_func(f)

    assert key_frequency_counter == Counter({"key1": 2, "key2": 3, "key3": 1})