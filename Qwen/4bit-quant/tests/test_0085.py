import pytest
from src_0085 import task_func

def test_task_func_no_products():
    result = task_func([])
    assert result.empty
    assert list(result.columns) == ["Product", "Sales", "Profit"]

def test_task_func_invalid_products_type():
    with pytest.raises(TypeError):
        task_func(123)

def test_task_func_invalid_products_content():
    with pytest.raises(TypeError):
        task_func(["product1", 123])

def test_task_func_invalid_n_samples_type():
    with pytest.raises(ValueError):
        task_func(["product1"], n_samples="100")

def test_task_func_invalid_n_samples_value():
    with pytest.raises(ValueError):
        task_func(["product1"], n_samples=-10)

def test_task_func_invalid_sales_range():
    with pytest.raises(ValueError):
        task_func(["product1"], sales_lower=200, sales_upper=50)

def test_task_func_invalid_profit_margin():
    with pytest.raises(ValueError):
        task_func(["product1"], profit_margin_min=0.5, profit_margin_max=0.1)

def test_task_func_valid_input():
    result = task_func(["product1", "product2"], n_samples=5, random_seed=42)
    assert len(result) <= 2
    assert all(isinstance(row["Product"], str) for row in result.itertuples(index=False))
    assert all(isinstance(row["Sales"], int) for row in result.itertuples(index=False))
    assert all(isinstance(row["Profit"], (int, float)) for row in result.itertuples(index=False))

def test_task_func_grouping_and_sorting():
    result = task_func(["product1", "product2"], n_samples=10, random_seed=42)
    assert result.is_unique
    assert result["Profit"].is_monotonic_decreasing

def test_task_func_randomness():
    result1 = task_func(["product1", "product2"], n_samples=10, random_seed=42)
    result2 = task_func(["product1", "product2"], n_samples=10, random_seed=42)
    assert result1.equals(result2)