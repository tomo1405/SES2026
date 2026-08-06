import pytest
from src_0922 import task_func

def test_task_func():
    # Test case 1: Normalize a single column
    data = [[1, 2], [3, 4]]
    columns = ['A']
    expected_output = [[0.5, 1], [1.5, 2]]
    assert task_func(data, columns).equals(expected_output)

    # Test case 2: Normalize multiple columns
    data = [[1, 2, 3], [4, 5, 6]]
    columns = ['A', 'B']
    expected_output = [[0.5, 1, 1.5], [1.5, 2, 2.5]]
    assert task_func(data, columns).equals(expected_output)

    # Test case 3: Normalize a single row
    data = [[1, 2, 3]]
    columns = ['A', 'B']
    expected_output = [[0.5, 1, 1.5]]
    assert task_func(data, columns).equals(expected_output)

    # Test case 4: Normalize a single value
    data = [1]
    columns = ['A']
    expected_output = [0.5]
    assert task_func(data, columns).equals(expected_output)

    # Test case 5: Normalize a list of values
    data = [1, 2, 3]
    columns = ['A']
    expected_output = [0.5, 1, 1.5]
    assert task_func(data, columns).equals(expected_output)

    # Test case 6: Normalize a DataFrame with multiple columns
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    columns = ['A', 'B']
    expected_output = pd.DataFrame({'A': [0.5, 1, 1.5], 'B': [1.5, 2, 2.5]})
    assert task_func(data, columns).equals(expected_output)

    # Test case 7: Normalize a DataFrame with a single column
    data = pd.DataFrame({'A': [1, 2, 3]})
    columns = ['A']
    expected_output = pd.DataFrame({'A': [0.5, 1, 1.5]})
    assert task_func(data, columns).equals(expected_output)

    # Test case 8: Normalize a DataFrame with a single row
    data = pd.DataFrame({'A': [1, 2, 3]})
    columns = ['A']
    expected_output = pd.DataFrame({'A': [0.5, 1, 1.5]})
    assert task_func(data, columns).equals(expected_output)

    # Test case 9: Normalize a DataFrame with a single value
    data = pd.DataFrame({'A': [1]})
    columns = ['A']
    expected_output = pd.DataFrame({'A': [0.5]})
    assert task_func(data, columns).equals(expected_output)

    # Test case 10: Normalize a DataFrame with a list of values
    data = pd.DataFrame({'A': [1, 2, 3]})
    columns = ['A']
    expected_output = pd.DataFrame({'A': [0.5, 1, 1.5]})
    assert task_func(data, columns).equals(expected_output)