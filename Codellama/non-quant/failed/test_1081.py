import pytest
from src_1081 import task_func

def test_task_func():
    # Test case 1: Area string is "1,000"
    area_string = "1,000"
    expected_price = 100
    assert task_func(area_string) == expected_price

    # Test case 2: Area string is "2,000"
    area_string = "2,000"
    expected_price = 200
    assert task_func(area_string) == expected_price

    # Test case 3: Area string is "3,000"
    area_string = "3,000"
    expected_price = 300
    assert task_func(area_string) == expected_price

    # Test case 4: Area string is "4,000"
    area_string = "4,000"
    expected_price = 400
    assert task_func(area_string) == expected_price

    # Test case 5: Area string is "5,000"
    area_string = "5,000"
    expected_price = 500
    assert task_func(area_string) == expected_price

    # Test case 6: Area string is "6,000"
    area_string = "6,000"
    expected_price = 600
    assert task_func(area_string) == expected_price

    # Test case 7: Area string is "7,000"
    area_string = "7,000"
    expected_price = 700
    assert task_func(area_string) == expected_price

    # Test case 8: Area string is "8,000"
    area_string = "8,000"
    expected_price = 800
    assert task_func(area_string) == expected_price

    # Test case 9: Area string is "9,000"
    area_string = "9,000"
    expected_price = 900
    assert task_func(area_string) == expected_price

    # Test case 10: Area string is "10,000"
    area_string = "10,000"
    expected_price = 1000
    assert task_func(area_string) == expected_price