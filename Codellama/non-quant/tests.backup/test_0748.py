import pytest
from src_0748 import task_func

def test_task_func():
    # Test case 1: Empty string
    assert task_func("") == (0, 0)

    # Test case 2: Single number
    assert task_func("123") == (1, 11.180339887498949)

    # Test case 3: Multiple numbers
    assert task_func("123 456 789") == (3, 11.180339887498949)

    # Test case 4: Decimal numbers
    assert task_func("123.456 789.012") == (2, 11.180339887498949)

    # Test case 5: Negative numbers
    assert task_func("-123 -456 -789") == (3, 11.180339887498949)

    # Test case 6: Mixed numbers
    assert task_func("123.456 -789 0.012") == (3, 11.180339887498949)

    # Test case 7: Non-numeric characters
    assert task_func("abc123def456ghi789") == (3, 11.180339887498949)

    # Test case 8: Empty string with spaces
    assert task_func("   ") == (0, 0)

    # Test case 9: String with only spaces
    assert task_func("   ") == (0, 0)

    # Test case 10: String with only tabs
    assert task_func("\t\t\t") == (0, 0)

    # Test case 11: String with only newlines
    assert task_func("\n\n\n") == (0, 0)

    # Test case 12: String with only carriage returns
    assert task_func("\r\r\r") == (0, 0)

    # Test case 13: String with only null characters
    assert task_func("\0\0\0") == (0, 0)

    # Test case 14: String with only non-printable characters
    assert task_func("\x01\x02\x03") == (0, 0)

    # Test case 15: String with only non-ASCII characters
    assert task_func("áéíóú") == (0, 0)