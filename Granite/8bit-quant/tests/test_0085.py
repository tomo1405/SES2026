import pandas as pd
import pytest
from src_0085 import task_func


def test_task_func():
    # Test case 1: No products
    expected_df = pd.DataFrame(columns=["Product", "Sales", "Profit"])
    actual_df = task_func([])
    assert actual_df.equals(expected_df)

    # Test case 2: Invalid products
    with pytest.raises(TypeError):
        task_func(123)
    with pytest.raises(TypeError):
        task_func(["product1", 123])

    # Test case 3: Invalid n_samples
    with pytest.raises(ValueError):
        task_func(["product1", "product2"], n_samples=-1)
    with pytest.raises(TypeError):
        task_func(["product1", "product2"], n_samples="abc")

    # Test case 4: Invalid sales_lower and sales_upper
    with pytest.raises(ValueError):
        task_func(["product1", "product2"], sales_lower=200, sales_upper=100)
    with pytest.raises(TypeError):
        task_func(["product1", "product2"], sales_lower="abc", sales_upper=100)
    with pytest.raises(TypeError):
        task_func(["product1", "product2"], sales_lower=200, sales_upper="def")

    # Test case 5: Invalid profit_margin_min and profit_margin_max
    with pytest.raises(ValueError):
        task_func(["product1", "product2"], profit_margin_min=0.5, profit_margin_max=0.1)
    with pytest.raises(TypeError):
        task_func(["product1", "product2"], profit_margin_min="abc", profit_margin_max=0.1)
    with pytest.raises(TypeError):
        task_func(["product1", "product2"], profit_margin_min=0.5, profit_margin_max="def")

    # Test case 6: Valid input
    products = ["product1", "product2", "product3"]
    n_samples = 100
    sales_lower = 50
    sales_upper = 200
    profit_margin_min = 0.1
    profit_margin_max = 0.5
    random_seed = 42
    expected_df = pd.DataFrame(columns=["Product", "Sales", "Profit"])
    actual_df = task_func(products, n_samples, sales_lower, sales_upper, profit_margin_min, profit_margin_max, random_seed)
    assert actual_df.equals(expected_df)