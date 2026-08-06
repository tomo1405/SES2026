import pytest
from src_0866 import task_func

def test_task_func():
    # Test case 1: Normal input
    data = [('A', 10, 100), ('B', 20, 200), ('C', 30, 300)]
    expected_output = pd.DataFrame({
        'Item': ['A', 'B', 'C'],
        'Normalized Count': [0.0, 0.0, 0.0],
        'Normalized Weight': [0.0, 0.0, 0.0]
    })
    assert task_func(data).equals(expected_output)

    # Test case 2: Input with negative values
    data = [('A', -10, 100), ('B', 20, -200), ('C', 30, 300)]
    expected_output = pd.DataFrame({
        'Item': ['A', 'B', 'C'],
        'Normalized Count': [-1.0, 0.0, 1.0],
        'Normalized Weight': [0.0, -1.0, 1.0]
    })
    assert task_func(data).equals(expected_output)

    # Test case 3: Input with zero values
    data = [('A', 0, 100), ('B', 20, 0), ('C', 30, 300)]
    expected_output = pd.DataFrame({
        'Item': ['A', 'B', 'C'],
        'Normalized Count': [0.0, 0.0, 1.0],
        'Normalized Weight': [0.0, 0.0, 1.0]
    })
    assert task_func(data).equals(expected_output)

    # Test case 4: Input with missing values
    data = [('A', 10, 100), ('B', 20, None), ('C', 30, 300)]
    expected_output = pd.DataFrame({
        'Item': ['A', 'B', 'C'],
        'Normalized Count': [0.0, 0.0, 1.0],
        'Normalized Weight': [0.0, 0.0, 1.0]
    })
    assert task_func(data).equals(expected_output)

    # Test case 5: Input with duplicate values
    data = [('A', 10, 100), ('B', 20, 200), ('C', 30, 300), ('A', 10, 100)]
    expected_output = pd.DataFrame({
        'Item': ['A', 'B', 'C', 'A'],
        'Normalized Count': [0.0, 0.0, 1.0, 0.0],
        'Normalized Weight': [0.0, 0.0, 1.0, 0.0]
    })
    assert task_func(data).equals(expected_output)