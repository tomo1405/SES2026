import pytest
from src_0062 import task_func

def test_task_func():
    result = [
        {'from_user': 1},
        {'from_user': 4},
        {'from_user': 9},
        {'from_user': 16}
    ]
    expected_square_roots = [1, 2, 3, 4]
    expected_title = 'Square root plot'
    expected_x_label = 'x'
    expected_y_label = 'sqrt(x)'
    expected_annotation = '2023-03-14 12:34:56'
    square_roots, ax = task_func(result)
    assert square_roots == expected_square_roots
    assert ax.get_title() == expected_title
    assert ax.get_xlabel() == expected_x_label
    assert ax.get_ylabel() == expected_y_label
    assert ax.annotations[0].get_text() == expected_annotation