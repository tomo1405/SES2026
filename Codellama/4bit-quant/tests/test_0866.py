import pandas as pd
from src_0866 import task_func


def test_task_func():
    # Test case 1: input data is a list of tuples
    data = [('item1', 10, 100), ('item2', 20, 200), ('item3', 30, 300)]
    expected_output = pd.DataFrame({
        'Item': ['item1', 'item2', 'item3'],
        'Normalized Count': [0.0, 0.0, 0.0],
        'Normalized Weight': [0.0, 0.0, 0.0]
    })
    assert task_func(data).equals(expected_output)

    # Test case 2: input data is a list of tuples with different lengths
    data = [('item1', 10, 100), ('item2', 20, 200), ('item3', 30, 300), ('item4', 40, 400)]
    expected_output = pd.DataFrame({
        'Item': ['item1', 'item2', 'item3', 'item4'],
        'Normalized Count': [0.0, 0.0, 0.0, 0.0],
        'Normalized Weight': [0.0, 0.0, 0.0, 0.0]
    })
    assert task_func(data).equals(expected_output)

    # Test case 3: input data is a list of tuples with different lengths
    data = [('item1', 10, 100), ('item2', 20, 200), ('item3', 30, 300), ('item4', 40, 400), ('item5', 50, 500)]
    expected_output = pd.DataFrame({
        'Item': ['item1', 'item2', 'item3', 'item4', 'item5'],
        'Normalized Count': [0.0, 0.0, 0.0, 0.0, 0.0],
        'Normalized Weight': [0.0, 0.0, 0.0, 0.0, 0.0]
    })
    assert task_func(data).equals(expected_output)