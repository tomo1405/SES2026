python
import pytest
from src_0085 import task_func

def test_task_func():
    # Test case 1: Empty list of products
    products = []
    n_samples = 100
    sales_lower = 50
    sales_upper = 200
    profit_margin_min = 0.1
    profit_margin_max = 0.5
    random_seed = 42
    expected_result = pd.DataFrame(columns=["Product", "Sales", "Profit"])
    assert task_func(products, n_samples, sales_lower, sales_upper, profit_margin_min, profit_margin_max, random_seed).equals(expected_result)

    # Test case 2: Non-empty list of products, valid inputs
    products = ["Product A", "Product B", "Product C"]
    n_samples = 100
    sales_lower = 50
    sales_upper = 200
    profit_margin_min = 0.1
    profit_margin_max = 0.5
    random_seed = 42
    expected_result = pd.DataFrame({"Product": ["Product A", "Product B", "Product C"], "Sales": [111, 121, 131], "Profit": [55.5, 60.6, 65.7]}).sort_values("Profit", ascending=False)
    assert task_func(products, n_samples, sales_lower, sales_upper, profit_margin_min, profit_margin_max, random_seed).equals(expected_result)

    # Test case 3: Non-empty list of products, invalid inputs
    products = ["Product A", "Product B", "Product C"]
    n_samples = -100
    sales_lower = 200
    sales_upper = 50
    profit_margin_min = 0.5
    profit_margin_max = 0.1
    random_seed = "42"
    with pytest.raises(ValueError):
        task_func(products, n_samples, sales_lower, sales_upper, profit_margin_min, profit_margin_max, random_seed)

    # Test case 4: Non-empty list of products, invalid inputs
    products = ["Product A", "Product B", "Product C"]
    n_samples = 100
    sales_lower = 50
    sales_upper = 200
    profit_margin_min = 0.5
    profit_margin_max = 0.1
    random_seed = 42
    with pytest.raises(ValueError):
        task_func(products, n_samples, sales_lower, sales_upper, profit_margin_min, profit_margin_max, random_seed)

    # Test case 5: Non-empty list of products, invalid inputs
    products = ["Product A", "Product B", "Product C"]
    n_samples = 100
    sales_lower = 50
    sales_upper = 200
    profit_margin_min = 0.1
    profit_margin_max = 0.5
    random_seed = 42
    with pytest.raises(TypeError):
        task_func(123, n_samples, sales_lower, sales_upper, profit_margin_min, profit_margin_max, random_seed)

    # Test case 6: Non-empty list of products, invalid inputs
    products = ["Product A", "Product B", "Product C"]
    n_samples = 100
    sales_lower = 50
    sales_upper = 200
    profit_margin_min = 0.1
    profit_margin_max = 0.5
    random_seed = 42
    with pytest.raises(TypeError):
        task_func("Product A, Product B, Product C", n_samples, sales_lower, sales_upper, profit_margin_min, profit_margin_max, random_seed)