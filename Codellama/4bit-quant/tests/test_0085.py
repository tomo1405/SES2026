import pandas as pd
from src_0085 import task_func


def test_task_func():
    products = ["Product A", "Product B", "Product C"]
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
    assert all(df["Sales"].between(sales_lower, sales_upper))
    assert all(df["Profit"].between(sales_lower * profit_margin_min, sales_upper * profit_margin_max))
    assert all(df["Profit"].div(df["Sales"]).between(profit_margin_min, profit_margin_max))
    assert df.groupby("Product").sum().shape[0] == len(products)
    assert df.groupby("Product").sum().shape[1] == 3
    assert df.groupby("Product").sum().columns[0] == "Product"
    assert df.groupby("Product").sum().columns[1] == "Sales"
    assert df.groupby("Product").sum().columns[2] == "Profit"
    assert all(df.groupby("Product").sum()["Profit"].between(sales_lower * profit_margin_min, sales_upper * profit_margin_max))
    assert all(df.groupby("Product").sum()["Profit"].div(df.groupby("Product").sum()["Sales"]).between(profit_margin_min, profit_margin_max))