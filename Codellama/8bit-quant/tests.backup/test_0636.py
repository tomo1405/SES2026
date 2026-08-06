import pytest
from src_0636 import task_func

def test_task_func():
    # Test case 1: Empty input
    text = ''
    n = 2
    expected_output = pd.DataFrame()
    actual_output, ax = task_func(text, n)
    assert actual_output.equals(expected_output)
    assert ax.get_figure().get_size_inches() == (8, 6)

    # Test case 2: Non-empty input
    text = 'This is a sample text'
    n = 2
    expected_output = pd.DataFrame({'This': [1, 0, 0], 'is': [0, 1, 0], 'a': [0, 0, 1], 'sample': [0, 0, 1], 'text': [0, 0, 1]})
    actual_output, ax = task_func(text, n)
    assert actual_output.equals(expected_output)
    assert ax.get_figure().get_size_inches() == (8, 6)

    # Test case 3: n = 3
    text = 'This is a sample text'
    n = 3
    expected_output = pd.DataFrame({'This is': [1, 0, 0], 'is a': [0, 1, 0], 'a sample': [0, 0, 1], 'sample text': [0, 0, 1]})
    actual_output, ax = task_func(text, n)
    assert actual_output.equals(expected_output)
    assert ax.get_figure().get_size_inches() == (8, 6)