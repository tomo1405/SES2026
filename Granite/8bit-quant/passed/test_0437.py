import pytest
from src_0437 import task_func

def test_task_func():
    with pytest.raises(TypeError):
        task_func(123)  # Test if TypeError is raised for non-string input

    input_str = "Hello, World!"
    result = task_func(input_str)
    assert isinstance(result, tuple) and len(result) == 2
    letter_counts, ax = result
    assert isinstance(letter_counts, dict)
    assert all(isinstance(letter, str) and isinstance(count, int) for letter, count in letter_counts.items())
    assert isinstance(ax, object)