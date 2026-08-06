import pytest
from src_0493 import task_func

def test_task_func():
    epoch_milliseconds = 1648880000000
    random_seed = 0
    products = ["Product1", "Product2", "Product3", "Product4", "Product5"]

    df = task_func(epoch_milliseconds, random_seed, products)

    assert df.shape == (5, 3)
    assert df.columns.tolist() == ["Product", "Date", "Sales"]
    assert df["Product"].isin(products).all()
    assert df["Date"].dtype == "datetime64[ns]"
    assert df["Sales"].dtype == "int64"
    assert df["Sales"].between(10, 50).all()

def test_task_func_invalid_products():
    epoch_milliseconds = 1648880000000
    random_seed = 0
    products = ["Product1", "Product2", "Product3", "Product4"]

    with pytest.raises(ValueError):
        task_func(epoch_milliseconds, random_seed, products)

def test_task_func_invalid_start_time():
    epoch_milliseconds = 1648880000000
    random_seed = 0
    products = ["Product1", "Product2", "Product3", "Product4", "Product5"]

    with pytest.raises(ValueError):
        task_func(epoch_milliseconds, random_seed, products)