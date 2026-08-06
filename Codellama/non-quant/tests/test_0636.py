import pandas as pd
from src_0636 import task_func


def test_task_func():
    # Test case 1: Empty input
    text = ''
    n = 2
    expected_output = pd.DataFrame()
    actual_output = task_func(text, n)
    assert actual_output == expected_output

    # Test case 2: Non-empty input
    text = 'This is a sample text'
    n = 2
    expected_output = pd.DataFrame({'This': [1, 0, 0], 'is': [0, 1, 0], 'a': [0, 0, 1], 'sample': [0, 0, 1], 'text': [0, 0, 1]})
    actual_output = task_func(text, n)
    assert actual_output == expected_output

    # Test case 3: n = 3
    text = 'This is a sample text'
    n = 3
    expected_output = pd.DataFrame({'This is': [1, 0, 0], 'is a': [0, 1, 0], 'a sample': [0, 0, 1], 'sample text': [0, 0, 1]})
    actual_output = task_func(text, n)
    assert actual_output == expected_output

    # Test case 4: n = 4
    text = 'This is a sample text'
    n = 4
    expected_output = pd.DataFrame({'This is a': [1, 0, 0], 'is a sample': [0, 1, 0], 'a sample text': [0, 0, 1]})
    actual_output = task_func(text, n)
    assert actual_output == expected_output

    # Test case 5: n = 5
    text = 'This is a sample text'
    n = 5
    expected_output = pd.DataFrame({'This is a sample': [1, 0, 0], 'is a sample text': [0, 1, 0]})
    actual_output = task_func(text, n)
    assert actual_output == expected_output