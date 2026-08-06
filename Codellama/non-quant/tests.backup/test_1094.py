import pytest
from src_1094 import task_func

def test_task_func():
    text_file = "test_data.txt"
    with open(text_file, 'w') as file:
        file.write("""
        {
            "key1": "value1",
            "key2": "value2",
            "key3": {
                "key31": "value31",
                "key32": "value32"
            }
        }
        """)

    results = task_func(text_file)

    assert len(results) == 1
    assert results[0] == {
        "key1": "value1",
        "key2": "value2",
        "key3": {
            "key31": "value31",
            "key32": "value32"
        }
    }

    # Clean up test data
    os.remove(text_file)