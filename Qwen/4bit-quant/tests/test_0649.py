from src_0649 import task_func


def test_task_func_next_business_day():
    # Test with a date that is a Saturday
    assert task_func("2023-10-07") == parse("2023-10-09")

    # Test with a date that is a Sunday
    assert task_func("2023-10-08") == parse("2023-10-09")

    # Test with a date that is already a Monday
    assert task_func("2023-10-09") == parse("2023-10-10")

    # Test with a date that is a Friday
    assert task_func("2023-10-13") == parse("2023-10-16")

    # Test with a date that is a Wednesday
    assert task_func("2023-10-11") == parse("2023-10-12")

    # Test with a date that is a Tuesday
    assert task_func("2023-10-10") == parse("2023-10-11")

    # Test with a date that is a Monday (edge case)
    assert task_func("2023-10-09") == parse("2023-10-10")

    # Test with a date that is a Saturday (edge case)
    assert task_func("2023-10-07") == parse("2023-10-09")

    # Test with a date that is a Sunday (edge case)
    assert task_func("2023-10-08") == parse("2023-10-09")