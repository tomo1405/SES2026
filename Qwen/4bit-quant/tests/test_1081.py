import pytest
from src_1081 import task_func

def test_task_func():
    # Test with a known value from the DATA dictionary
    area_string = "3,000"
    expected_price = 300
    assert task_func(area_string) == expected_price

    # Test with a different value
    area_string = "6,000"
    # Assuming linear relationship, price should be 600
    expected_price = 600
    assert task_func(area_string) == expected_price

    # Test with a very small area
    area_string = "100"
    # Assuming linear relationship, price should be 10
    expected_price = 10
    assert task_func(area_string) == expected_price

    # Test with a very large area
    area_string = "10,000"
    # Assuming linear relationship, price should be 1000
    expected_price = 1000
    assert task_func(area_string) == expected_price

    # Test with a decimal area
    area_string = "2,500"
    # Assuming linear relationship, price should be 250
    expected_price = 250
    assert task_func(area_string) == expected_price

    # Test with a negative area (edge case, but valid input)
    area_string = "-500"
    # Assuming linear relationship, price should be -50
    expected_price = -50
    assert task_func(area_string) == expected_price

# Run the tests
if __name__ == "__main__":
    pytest.main()