import pytest
from src_0085 import task_func
import numpy as np
import pandas as pd

def test_task_func_no_products():
    result = task_func([])
    assert result.equals(pd.DataFrame(columns=["Product", "Sales", "Profit"]))

def test_task_func_invalid_products_type():
    with pytest.raises(TypeError):
        task_func(123)

def test_task_func_invalid_products_elements():
    with pytest.raises(TypeError):
        task_func(["product1", 2, "product3"])

def test_task_func_invalid_n_samples_type():
    with pytest.raises(ValueError):
        task_func(["product1"], n_samples="100")

def test_task_func_invalid_n_samples_value():
    with pytest.raises(ValueError):
        task_func(["product1"], n_samples=-10)

def test_task_func_invalid_sales_lower_type():
    with pytest.raises(ValueError):
        task_func(["product1"], sales_lower="50")

def test_task_func_invalid_sales_upper_type():
    with pytest.raises(ValueError):
        task_func(["product1"], sales_upper="200")

def test_task_func_invalid_sales_lower_greater_than_upper():
    with pytest.raises(ValueError):
        task_func(["product1"], sales_lower=200, sales_upper=50)

def test_task_func_invalid_profit_margin_min_type():
    with pytest.raises(ValueError):
        task_func(["product1"], profit_margin_min="0.1")

def test_task_func_invalid_profit_margin_max_type():
    with pytest.raises(ValueError):
        task_func(["product1"], profit_margin_max="0.5")

def test_task_func_invalid_profit_margin_min_greater_than_max():
    with pytest.raises(ValueError):
        task_func(["product1"], profit_margin_min=0.5, profit_margin_max=0.1)

def test_task_func_valid_input():
    np.random.seed(42)
    result = task_func(["product1", "product2"], n_samples=5)
    expected_columns = ["Product", "Sales", "Profit"]
    assert list(result.columns) == expected_columns
    assert len(result) <= 2  # Since we are grouping by product, there can be at most 2 rows
    assert result["Sales"].dtype == np.int64
    assert result["Profit"].dtype == np.float64

def test_task_func_result_order():
    np.random.seed(42)
    result = task_func(["product1", "product2"], n_samples=5)
    assert result.iloc[0]["Profit"] >= result.iloc[-1]["Profit"]

def test_task_func_random_seed_consistency():
    np.random.seed(42)
    result1 = task_func(["product1", "product2"], n_samples=5)
    np.random.seed(42)
    result2 = task_func(["product1", "product2"], n_samples=5)
    assert result1.equals(result2)