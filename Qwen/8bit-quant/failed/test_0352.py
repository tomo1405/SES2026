import pytest
from src_0352 import task_func

def test_task_func():
    product_list = ['ProductA', 'ProductB', 'ProductC']
    categories = ['Category1', 'Category2', 'Category3']

    # Test with default parameters
    df = task_func(product_list, categories)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(product_list)
    assert all(col in df.columns for col in ['Product', 'Category', 'Quantity Sold', 'Revenue'])

    # Test with custom min and max values
    df_custom = task_func(product_list, categories, min_value=5, max_value=50)
    assert isinstance(df_custom, pd.DataFrame)
    assert len(df_custom) == len(product_list)
    assert all(col in df_custom.columns for col in ['Product', 'Category', 'Quantity Sold', 'Revenue'])

    # Test with empty product list
    df_empty_products = task_func([], categories)
    assert df_empty_products.empty

    # Test with empty categories
    with pytest.raises(IndexError):
        task_func(product_list, [])

    # Test with single product and category
    df_single = task_func(['SingleProduct'], ['SingleCategory'])
    assert len(df_single) == 1
    assert df_single.iloc[0]['Product'] == 'SingleProduct'
    assert df_single.iloc[0]['Category'] == 'SingleCategory'