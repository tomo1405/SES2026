import pytest
from src_0085 import task_func

def test_task_func_valid_input():
    products = ["A", "B", "C"]
    n_samples = 100
    sales_lower = 50
    sales_upper = 200
    profit_margin_min = 0.1
    profit_margin_max = 0.5
    random_seed = 42

    df = task_func(products, n_samples, sales_lower, sales_upper, profit_margin_min, profit_margin_max, random_seed)

    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] == n_samples
    assert df.shape[1] == 3
    assert "Product" in df.columns
    assert "Sales" in df.columns
    assert "Profit" in df.columns
    assert all(df["Product"].isin(products))
    assert all(df["Sales"] >= sales_lower)
    assert all(df["Sales"] <= sales_upper)
    assert all(df["Profit"] >= profit_margin_min * df["Sales"])
    assert all(df["Profit"] <= profit_margin_max * df["Sales"])

def test_task_func_invalid_input():
    products = ["A", "B", "C"]
    n_samples = 100
    sales_lower = 50
    sales_upper = 200
    profit_margin_min = 0.1
    profit_margin_max = 0.5
    random_seed = 42

    with pytest.raises(TypeError):
        task_func(products, n_samples, sales_lower, sales_upper, profit_margin_min, profit_margin_max, random_seed, invalid_param=True)

    with pytest.raises(ValueError):
        task_func(products, n_samples, sales_lower, sales_upper, profit_margin_min, profit_margin_max, random_seed, n_samples=-1)

    with pytest.raises(ValueError):
        task_func(products, n_samples, sales_lower, sales_upper, profit_margin_min, profit_margin_max, random_seed, sales_lower=101)

    with pytest.raises(ValueError):
        task_func(products, n_samples, sales_lower, sales_upper, profit_margin_min, profit_margin_max, random_seed, sales_upper=99)

    with pytest.raises(ValueError):
        task_func(products, n_samples, sales_lower, sales_upper, profit_margin_min, profit_margin_max, random_seed, profit_margin_min=0.6)

    with pytest.raises(ValueError):
        task_func(products, n_samples, sales_lower, sales_upper, profit_margin_min, profit_margin_max, random_seed, profit_margin_max=0.4)