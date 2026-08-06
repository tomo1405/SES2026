import pytest
from src_0096 import task_func

def test_task_func():
    # Test with default values
    sales_df = task_func()
    assert isinstance(sales_df, pd.DataFrame)
    assert sales_df.shape == (12, 3)
    assert set(sales_df.columns) == {'Month', 'Category', 'Sales'}
    assert set(sales_df['Month'].unique()) == {'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'}
    assert set(sales_df['Category'].unique()) == {'Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Beauty & Personal Care'}
    assert sales_df['Sales'].min() >= 100
    assert sales_df['Sales'].max() <= 500

    # Test with custom values
    sales_df = task_func(categories=['Toys', 'Games'], months=['January', 'February'])
    assert isinstance(sales_df, pd.DataFrame)
    assert sales_df.shape == (2, 3)
    assert set(sales_df.columns) == {'Month', 'Category', 'Sales'}
    assert set(sales_df['Month'].unique()) == {'January', 'February'}
    assert set(sales_df['Category'].unique()) == {'Toys', 'Games'}
    assert sales_df['Sales'].min() >= 100
    assert sales_df['Sales'].max() <= 500

    # Test with invalid values
    with pytest.raises(ValueError):
        task_func(categories=[], months=['January'])
    with pytest.raises(ValueError):
        task_func(categories=['Toys', 'Games'], months=[])