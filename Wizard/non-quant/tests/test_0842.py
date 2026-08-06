python
import json
import pytest
from src_0842 import task_func

def test_task_func():
    # Test case 1: Valid JSON input
    json_string = '{"text": "The quick brown fox jumps over the lazy dog."}'
    expected_output = {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
    assert task_func(json_string) == expected_output

    # Test case 2: Invalid JSON input
    json_string = '{"text": "This is not valid JSON"}'
    expected_output = {}
    assert task_func(json_string) == expected_output

    # Test case 3: Empty JSON input
    json_string = '{}'
    expected_output = {}
    assert task_func(json_string) == expected_output

    # Test case 4: JSON input with no text field
    json_string = '{"not_text": "This is not a text field"}'
    expected_output = {}
    assert task_func(json_string) == expected_output

    # Test case 5: JSON input with no text field and no other fields
    json_string = '{}'
    expected_output = {}
    assert task_func(json_string) == expected_output