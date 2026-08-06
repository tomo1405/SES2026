import pandas as pd
from src_0952 import task_func


def test_task_func():
    mystrings = ['Product 1', 'Product 2', 'Product 3']
    n_products = 3
    seed = 0
    expected_output = pd.DataFrame({'Product Name': ['Product_1', 'Product_2', 'Product_3'],
                                   'Category': ['Electronics', 'Clothing', 'Home & Kitchen'],
                                   'Price': [50.0, 50.0, 50.0]})
    output = task_func(mystrings, n_products, seed)
    pd.testing.assert_frame_equal(output, expected_output)