python
import collections
import json
import os
import pytest

from src_0289 import task_func

def test_task_func():
    directory_path = 'data'
    expected_result = {'key1': 2, 'key2': 1, 'key3': 1}

    result = task_func(directory_path)

    assert result == expected_result