import pytest
from src_0869 import task_func

def test_task_func():
    # Test case 1: n_colors = 1
    assert task_func(1) == ['Red']

    # Test case 2: n_colors = 2
    assert task_func(2) == ['Red', 'Green']

    # Test case 3: n_colors = 3
    assert task_func(3) == ['Red', 'Green', 'Blue']

    # Test case 4: n_colors = 4
    assert task_func(4) == ['Red', 'Green', 'Blue', 'Yellow']

    # Test case 5: n_colors = 5
    assert task_func(5) == ['Red', 'Green', 'Blue', 'Yellow', 'Purple']

    # Test case 6: n_colors = 6
    assert task_func(6) == ['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red']

    # Test case 7: n_colors = 7
    assert task_func(7) == ['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red', 'Green']

    # Test case 8: n_colors = 8
    assert task_func(8) == ['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red', 'Green', 'Blue']

    # Test case 9: n_colors = 9
    assert task_func(9) == ['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red', 'Green', 'Blue', 'Yellow']

    # Test case 10: n_colors = 10
    assert task_func(10) == ['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red', 'Green', 'Blue', 'Yellow', 'Purple']

    # Test case 11: n_colors = 11
    assert task_func(11) == ['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red']

    # Test case 12: n_colors = 12
    assert task_func(12) == ['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red', 'Green']

    # Test case 13: n_colors = 13
    assert task_func(13) == ['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red', 'Green', 'Blue']

    # Test case 14: n_colors = 14
    assert task_func(14) == ['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red', 'Green', 'Blue', 'Yellow']

    # Test case 15: n_colors = 15
    assert task_func(15) == ['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red', 'Green', 'Blue', 'Yellow', 'Purple']

    # Test case 16: n_colors = 16
    assert task_func(16) == ['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red']

    # Test case 17: n_colors = 17
    assert task_func(17) == ['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red', 'Green']

    # Test case 18: n_colors = 18
    assert task_func(18) == ['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red', 'Green', 'Blue']

    # Test case 19: n_colors = 19
    assert task_func(19) == ['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red', 'Green', 'Blue', 'Yellow']

    # Test case 20: n_colors = 20
    assert task_func(20) == ['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Red', 'Green', 'Blue', 'Yellow', 'Purple']