import pandas as pd
import random
import pytest

from src_0350 import task_func

@pytest.fixture
def product_list():
    return ['Product1', 'Product2', 'Product3']

@pytest.fixture
def categories():
    return ['Category1', 'Category2', 'Category3', 'Category4', 'Category5']

def test_task_func(product_list, categories):
    report_df = task_func(product_list, categories)
    assert isinstance(report_df, pd.DataFrame)
    assert report_df.columns.tolist() == ['Product', 'Category', 'Quantity Sold', 'Revenue']
    assert len(report_df) == len(product_list)