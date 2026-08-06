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
                   ['January', 'Beauty & Personal Care', 130.7],
                   ['February', 'Electronics', 145.3],
                   ['February', 'Clothing', 160.2],
                   ['February', 'Home & Kitchen', 180.1],
                   ['February', 'Books', 120.6],
                   ['February', 'Beauty & Personal Care', 170.9],
                   # ... and so on
                   ['December', 'Beauty & Personal Care', 190.3]],
                  columns=['Month', 'Category', 'Sales']))
])
def test_task_func(categories, months, random_seed, expected_output):
    seed(random_seed)
    actual_output = task_func(categories, months, random_seed)
    assert actual_output.equals(expected_output)