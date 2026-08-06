import pytest
from src_0435 import task_func

def test_task_func():
    # Test 1: Empty string input
    with pytest.raises(ValueError):
        task_func("")

    # Test 2: Incomplete data input
    with pytest.raises(ValueError):
        task_func("1234567890")

    # Test 3: Valid input
    df = task_func("1234567890\n1234567890\n1234567890\n1234567890\n1234567890")
    assert df.shape == (5, 6)
    assert df.columns.tolist() == ["ID", "Quantity", "Code", "Price", "Product", "Description"]
    assert df["Quantity"].dtype == int
    assert df["Price"].dtype == int

    # Test 4: Valid input with seed
    df = task_func("1234567890\n1234567890\n1234567890\n1234567890\n1234567890", seed=123)
    assert df.shape == (5, 6)
    assert df.columns.tolist() == ["ID", "Quantity", "Code", "Price", "Product", "Description"]
    assert df["Quantity"].dtype == int
    assert df["Price"].dtype == int

    # Test 5: Valid input with seed and code_to_product
    df = task_func("1234567890\n1234567890\n1234567890\n1234567890\n1234567890", seed=123, code_to_product={"1234567890": "Apple"})
    assert df.shape == (5, 6)
    assert df.columns.tolist() == ["ID", "Quantity", "Code", "Price", "Product", "Description"]
    assert df["Quantity"].dtype == int
    assert df["Price"].dtype == int
    assert df["Product"].tolist() == ["Apple", "Apple", "Apple", "Apple", "Apple"]