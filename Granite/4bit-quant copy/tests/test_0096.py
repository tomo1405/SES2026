import pandas as pd
from random import randint, uniform, seed
from src_0096 import task_func
import pytest

def test_task_func():
    categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Beauty & Personal Care']
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    random_seed = 42
    seed(random_seed)  # Setting the seed for reproducibility
    sales_data = []

    for month in months:
        for category in categories:
            sales = randint(100, 500) + uniform(0, 1)
            sales_data.append([month, category, sales])

    sales_df = pd.DataFrame(sales_data, columns=['Month', 'Category', 'Sales'])
    result_df = task_func(categories, months, random_seed)
    assert result_df.equals(sales_df)

def test_task_func_invalid_categories():
    categories = ''
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    random_seed = 42
    with pytest.raises(ValueError) as exc_info:
        task_func(categories, months, random_seed)
    assert "Invalid 'categories': must be a non-empty list." in str(exc_info.value)

def test_task_func_invalid_months():
    categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Beauty & Personal Care']
    months = ''
    random_seed = 42
    with pytest.raises(ValueError) as exc_info:
        task_func(categories, months, random_seed)
    assert "Invalid 'months': must be a non-empty list." in str(exc_info.value)