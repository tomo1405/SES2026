import ast
import json
from collections import Counter
from io import StringIO

import pytest

from src_1091 import task_func

def test_task_func():
    data = [
        '{"a": 1, "b": 2}',
        '{"c": 3, "d": 4}',
        '{"e": 5, "f": 6}',
    ]
    file_pointer = StringIO('[\n' + ',\n'.join(data) + '\n]')

    result = task_func(file_pointer)

    assert result == Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1})

def test_task_func_with_invalid_data():
    data = [
        '{"a": 1, "b": 2}',
        '{"c": 3, "d": 4}',
        '{"e": 5, "f": 6}',
        'not a valid json string',
    ]
    file_pointer = StringIO('[\n' + ',\n'.join(data) + '\n]')

    result = task_func(file_pointer)

    assert result == Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1})