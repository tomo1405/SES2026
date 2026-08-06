import pytest
from src_0943 import task_func

def test_task_func():
    sales_df, ax = task_func()
    assert isinstance(sales_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert sales_df.shape == (13, 3)
    assert sales_df.columns.tolist() == ['Date', 'Category', 'Sales']
    assert sales_df['Date'].dtype == 'datetime64[ns]'
    assert sales_df['Category'].dtype == 'object'
    assert sales_df['Sales'].dtype == 'int64'
    assert sales_df['Sales'].min() >= 100
    assert sales_df['Sales'].max() <= 500
    assert ax.get_title() == 'Category-wise Sales Trends'
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Sales'
    assert ax.get_legend() == None
    assert ax.get_grid() == True