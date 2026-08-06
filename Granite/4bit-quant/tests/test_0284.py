import os
import json
from collections import Counter
from src_0284 import task_func

def test_task_func():
    # Test case 1: Test with an empty directory
    assert task_func() == {}

    # Test case 2: Test with a directory containing a single JSON file
    test_dir = 'test_dir'
    os.makedirs(test_dir, exist_ok=True)
    test_json = os.path.join(test_dir, 'test.json')
    with open(test_json, 'w') as f:
        json.dump({'name': 'Alice'}, f)
    assert task_func(test_dir) == {'Alice': 1}

    # Test case 3: Test with a directory containing multiple JSON files
    test_json_2 = os.path.join(test_dir, 'test2.json')
    with open(test_json_2, 'w') as f:
        json.dump({'name': 'Bob'}, f)
    assert task_func(test_dir) == {'Alice': 1, 'Bob': 1}

    # Clean up
    os.rmdir(test_dir)