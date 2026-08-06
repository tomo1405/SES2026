import numpy as np
import pandas as pd
import pytest
from src_0085 import task_func

def test_task_func_with_valid_input():
    products = ["Product A", "Product B", "Product C"]
    n_samples = 100
    sales_lower = 50
    sales_upper = 200
    profit_margin_min = 0.1
    profit_margin_max = 0.5
    random_seed = 42
    expected_df = pd.DataFrame({
        "Product": ["Product A", "Product B", "Product C"],
        "Sales": [145, 132, 178],
        "Profit": [145 * 0.45, 132 * 0.32, 178 * 0.49]
    })

    np.random.seed(random_seed)
    actual_df = task_func(products, n_samples, sales_lower, sales_upper, profit_margin_min, profit_margin_max, random_seed)

    pd.testing.assert_frame_equal(actual_df, expected_df)

def test_task_func_with_invalid_products():
    products = ["Product A", 123, "Product C"]
    n_samples = 100
    sales_lower = 50
    sales_upper = 200
    profit_margin_min = 0.1
    profit_margin_max = 0.5
    random_seed = 42

    with pytest.raises(TypeError) as exc_info:
        task_func(products, n_samples, sales_lower, sales_upper, profit_margin_min, profit_margin_max, random_seed)
    assert "products must be a list of strings." in str(exc_info.value)

def test_task_func_with_invalid_n_samples():
    products = ["Product A", "Product B", "Product C"]
    n_samples = -100
    sales_lower = 50
    sales_upper = 200
    profit_margin_min = 0.1
    profit_margin_max = 0.5
    random_seed = 42

    with pytest.raises(ValueError) as exc_info:
        task_func(products, n_samples, sales_lower, sales_upper, profit_margin_min, profit_margin_max, random_seed)
    assert "n_samples must be a positive integer." in str(exc_info.value)

def test_task_func_with_invalid_sales_range():
    products = ["Product A", "Product B", "Product C"]
    n_samples = 100
    sales_lower = 200
    sales_upper = 50
    profit_margin_min = 0.1
    profit_margin_max = 0.5
    random_seed = 42

    with pytest.raises(ValueError) as exc_info:
        task_func(products, n_samples, sales_lower, sales_upper, profit_margin_min, profit_margin_max, random_seed)
    assert "sales_lower must be less than sales_upper and both must be integers." in str(exc_info.value)

def test_task_func_with_invalid_profit_margin_range():
    products = ["Product A", "Product B", "Product C"]
    n_samples = 100
    sales_lower = 50
    sales_upper = 200
    profit_margin_min = 0.5
    profit_margin_max = 0.1
    random_seed = 42

    with pytest.raises(ValueError) as exc_info:
        task_func(products, n_samples, sales_lower, sales_upper, profit_margin_min, profit_margin_max, random_seed)
    assert "profit_margin_min must be less than profit_margin_max and both must be numeric." in str(exc_info.value)