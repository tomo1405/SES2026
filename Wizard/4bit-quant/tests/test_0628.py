python
import pytest
from src_0628 import task_func

def test_task_func():
    products_list = ['Product A', 'Product B', 'Product C']
    sales_df = task_func(products_list)

    assert isinstance(sales_df, pd.DataFrame)
    assert sales_df.shape == (3, 15)
    assert sales_df.columns.tolist() == ['Product'] + [f'Month {i+1}' for i in range(12)] + ['Average Sales']
    assert sales_df['Product'].tolist() == products_list
    assert all(sales_df[f'Month {i+1}'].apply(lambda x: isinstance(x, int)) for i in range(12))
    assert all(sales_df['Average Sales'].apply(lambda x: isinstance(x, float)) for i in range(3))