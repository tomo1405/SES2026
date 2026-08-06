import pytest
from src_0062 import task_func

def test_task_func():
    # Mock data
    result = [
        {'from_user': 1},
        {'from_user': 4},
        {'from_user': 9}
    ]

    expected_square_roots = [1, 2, 3]

    # Call the function
    square_roots, ax = task_func(result)

    # Check the output
    assert square_roots == expected_square_roots
    assert ax is not None

    # Additional assertions can be added to check the plot