import pytest
from src_0085 import task_func

def test_task_func_type_error():
    with pytest.raises(TypeError):
        task_func(products=None, n_samples=100, sales_lower=50, sales_upper=200, profit_margin_min=0.1, profit_margin_max=0.5, random_seed=42)

def test_task_func_value_error():
    with pytest.raises(ValueError):
        task_func(products=["A", "B", "C"], n_samples=0, sales_lower=50, sales_upper=200, profit_margin_min=0.1, profit_margin_max=0.5, random_seed=42)

    with pytest.raises(ValueError):
        task_func(products=["A", "B", "C"], n_samples=100, sales_lower=50, sales_upper=200, profit_margin_min=0.1, profit_margin_max=0.5, random_seed=42)

    with pytest.raises(ValueError):
        task_func(products=["A", "B", "C"], n_samples=100, sales_lower=50, sales_upper=200, profit_margin_min=0.1, profit_margin_max=0.5, random_seed=42)

def test_task_func_return_value():
    df = task_func(products=["A", "B", "C"], n_samples=100, sales_lower=50, sales_upper=200, profit_margin_min=0.1, profit_margin_max=0.5, random_seed=42)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 3)
    assert list(df.columns) == ["Product", "Sales", "Profit"]
    assert all(df["Product"].isin(["A", "B", "C"]))
    assert all(df["Sales"].between(50, 200))
    assert all(df["Profit"].between(50, 200))