import json
from collections import Counter
from io import StringIO

import pytest
from src_1091 import task_func


def test_task_func_with_empty_json():
    file_content = "[]"
    with StringIO(file_content) as f:
        result = task_func(f)
    assert result == Counter()

def test_task_func_with_single_dict():
    file_content = '[{"key1": "value1", "key2": "value2"}]'
    with StringIO(file_content) as f:
        result = task_func(f)
    assert result == Counter({'key1': 1, 'key2': 1})

def test_task_func_with_multiple_dicts():
    file_content = '[{"key1": "value1"}, {"key2": "value2"}, {"key1": "value3"}]'
    with StringIO(file_content) as f:
        result = task_func(f)
    assert result == Counter({'key1': 2, 'key2': 1})

def test_task_func_with_mixed_data_types():
    file_content = '["not a dict", {"key1": "value1"}, 123, {"key2": "value2"}]'
    with StringIO(file_content) as f:
        result = task_func(f)
    assert result == Counter({'key1': 1, 'key2': 1})

def test_task_func_with_nested_dicts():
    file_content = '[{"key1": {"nested_key1": "value1"}, "key2": "value2"}]'
    with StringIO(file_content) as f:
        result = task_func(f)
    assert result == Counter({'key1': 1, 'key2': 1})

def test_task_func_with_invalid_json():
    file_content = '{"invalid json"'
    with StringIO(file_content) as f:
        with pytest.raises(json.JSONDecodeError):
            task_func(f)

def test_task_func_with_string_items_that_are_dicts():
    file_content = '["{\\"key1\\": \\"value1\\"}", "{\\"key2\\": \\"value2\\"}"]'
    with StringIO(file_content) as f:
        result = task_func(f)
    assert result == Counter({'key1': 1, 'key2': 1})

def test_task_func_with_string_items_that_are_not_dicts():
    file_content = '["not a dict", "another not a dict"]'
    with StringIO(file_content) as f:
        result = task_func(f)
    assert result == Counter()