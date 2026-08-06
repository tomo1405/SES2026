import pytest
from src_0151 import task_func
import pandas as pd
import numpy as np

# Mock data for testing
product_dict = {
    'A': (10, 50),
    'B': (5, 30),
    'C': (7, 40)
}
product_keys = ['A', 'B', 'C']

def test_task_func():
    result = task_func(product_dict, product_keys)
    
    # Assertions to verify the output
    assert isinstance(result, tuple), "The function should return a tuple."
    df, ax = result
    assert isinstance(df, pd.DataFrame), "The first element of the tuple should be a DataFrame."
    assert isinstance(ax, type(None) or type(plt.gca())), "The second element of the tuple should be a matplotlib axis or None."
    assert len(df) == len(product_keys), "The DataFrame should have the same number of rows as the number of products."
    assert 'Average Price' in df.columns, "The DataFrame should have an 'Average Price' column."
    assert 'Average Profit' in df.columns, "The DataFrame should have an 'Average Profit' column."

pytest.main()