import pytest
from src_0748 import task_func

def test_task_func():
    # Test case 1: No numbers in input string
    assert task_func("") == (0, 0)

    # Test case 2: One number in input string
    assert task_func("123") == (1, math.sqrt(123))

    # Test case 3: Multiple numbers in input string
    assert task_func("123 456 789") == (3, math.sqrt(123) + math.sqrt(456) + math.sqrt(789))

    # Test case 4: Decimal numbers in input string
    assert task_func("123.456 789.012") == (2, math.sqrt(123.456) + math.sqrt(789.012))

    # Test case 5: Negative numbers in input string
    assert task_func("-123 456 -789") == (3, math.sqrt(123) + math.sqrt(456) + math.sqrt(789))

    # Test case 6: Zero in input string
    assert task_func("0") == (1, math.sqrt(0))

    # Test case 7: Empty string in input string
    assert task_func("") == (0, 0)

    # Test case 8: Non-numeric characters in input string
    assert task_func("abc") == (0, 0)

    # Test case 9: Multiple spaces in input string
    assert task_func("  123  456  ") == (2, math.sqrt(123) + math.sqrt(456))

    # Test case 10: Decimal point at the end of input string
    assert task_func("123.") == (1, math.sqrt(123))