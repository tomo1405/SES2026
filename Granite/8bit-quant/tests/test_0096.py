import pandas as pd
from random import randint, uniform, seed
from src_0096 import task_func
import pytest

@pytest.mark.parametrize("categories, months, random_seed, expected_output", [
    (['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Beauty & Personal Care'],
     ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
     42,
     pd.DataFrame([['January', 'Electronics', 102.4],
                   ['January', 'Clothing', 123.1],
                   ['January', 'Home & Kitchen', 150.5],
                   ['January', 'Books', 110.2],
                   ['January', 'Beauty & Personal Care', 135.7],
                   ['February', 'Electronics', 145.3],
                   ['February', 'Clothing', 167.2],
                   ['February', 'Home & Kitchen', 198.1],
                   ['February', 'Books', 150.8],
                   ['February', 'Beauty & Personal Care', 178.4],
                   # ... and so on for all months and categories
                   ['December', 'Beauty & Personal Care', 200.1]],
                  columns=['Month', 'Category', 'Sales']))
])
def test_task_func(categories, months, random_seed, expected_output):
    seed(random_seed)
    actual_output = task_func(categories, months, random_seed)
    assert actual_output.equals(expected_output)