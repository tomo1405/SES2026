python
import pytest
from src_0318 import task_func

def test_task_func():
    example_str = "This is a [test] string with [some] [special] [characters]!"
    expected_result = {'test': 0.5773502691896258, 'some': 0.5773502691896258, 'special': 0.5773502691896258, 'characters': 0.5773502691896258}
    result = task_func(example_str)
    assert result == expected_result