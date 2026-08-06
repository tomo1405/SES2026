from typing import Counter

from src_0762 import task_func


def test_task_func():
    # Test case 1: Empty input
    json_str = ""
    expected_output = {"data": {}, "value_counts": Counter()}
    assert task_func(json_str) == expected_output

    # Test case 2: Input with None values
    json_str = '{"key1": "value1", "key2": None, "key3": "value3"}'
    expected_output = {"data": {"key1": "value1", "key3": "value3"}, "value_counts": Counter({"value1": 1, "value3": 1})}
    assert task_func(json_str) == expected_output

    # Test case 3: Input with email addresses
    json_str = '{"key1": "value1", "key2": "email@example.com", "key3": "value3"}'
    expected_output = {"data": {"key1": "value1", "key3": "value3"}, "value_counts": Counter({"value1": 1, "value3": 1})}
    assert task_func(json_str) == expected_output

    # Test case 4: Input with multiple email addresses
    json_str = '{"key1": "value1", "key2": "email1@example.com", "key3": "email2@example.com"}'
    expected_output = {"data": {"key1": "value1"}, "value_counts": Counter({"value1": 1})}
    assert task_func(json_str) == expected_output

    # Test case 5: Input with multiple email addresses and None values
    json_str = '{"key1": "value1", "key2": "email1@example.com", "key3": "email2@example.com", "key4": None}'
    expected_output = {"data": {"key1": "value1"}, "value_counts": Counter({"value1": 1})}
    assert task_func(json_str) == expected_output