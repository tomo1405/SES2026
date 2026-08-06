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
    expected_output = pd.DataFrame([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    actual_output = task_func(text, n)
    assert actual_output == expected_output

    # Test case 3: n = 1
    text = 'This is a sample text'
    n = 1
    expected_output = pd.DataFrame([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    actual_output = task_func(text, n)
    assert actual_output == expected_output

    # Test case 4: n = 3
    text = 'This is a sample text'
    n = 3
    expected_output = pd.DataFrame([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    actual_output = task_func(text, n)
    assert actual_output == expected_output

    # Test case 5: n = 4
    text = 'This is a sample text'
    n = 4
    expected_output = pd.DataFrame([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    actual_output = task_func(text, n)
    assert actual_output == expected_output

    # Test case 6: n = 5
    text = 'This is a sample text'
    n = 5
    expected_output = pd.DataFrame([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    actual_output = task_func(text, n)
    assert actual_output == expected_output

    # Test case 7: n = 6
    text = 'This is a sample text'
    n = 6
    expected_output = pd.DataFrame([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    actual_output = task_func(text, n)
    assert actual_output == expected_output

    # Test case 8: n = 7
    text = 'This is a sample text'
    n = 7
    expected_output = pd.DataFrame([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    actual_output = task_func(text, n)
    assert actual_output == expected_output

    # Test case 9: n = 8
    text = 'This is a sample text'
    n = 8
    expected_output = pd.DataFrame([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    actual_output = task_func(text, n)
    assert actual_output == expected_output

    # Test case 10: n = 9
    text = 'This is a sample text'
    n = 9
    expected_output = pd.DataFrame([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    actual_output = task_func(text, n)
    assert actual_output == expected_output

    # Test case 11: n = 10
    text = 'This is a sample text'
    n = 10
    expected_output = pd.DataFrame([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    actual_output = task_func(text, n)
    assert actual_output == expected_output