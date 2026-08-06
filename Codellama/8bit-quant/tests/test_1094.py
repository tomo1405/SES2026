import pytest
from src_1094 import task_func

def test_task_func():
    text_file = "test_data.txt"
    expected_results = [
        {"key1": "value1", "key2": "value2"},
        {"key3": "value3", "key4": "value4"},
        {"key5": "value5", "key6": "value6"}
    ]

    with open(text_file, 'w') as file:
        file.write("""
        {
            "key1": "value1",
            "key2": "value2"
        }
        {
            "key3": "value3",
            "key4": "value4"
        }
        {
            "key5": "value5",
            "key6": "value6"
        }
        """)

    results = task_func(text_file)

    assert results == expected_results