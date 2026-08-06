import pytest
from src_1091 import task_func
import json
from collections import Counter
import ast

@pytest.fixture
def sample_data():
    return [
        '{"key1": "value1", "key2": "value2"}',
        '{"key3": "value3", "key4": "value4"}'
    ]

def test_task_func(sample_data):
    file_pointer = iter(sample_data)
    result = task_func(file_pointer=file_pointer)
    assert isinstance(result, Counter)
    assert len(result) == 4  # Assuming the keys are unique for the example

if __name__ == "__main__":
    pytest.main()