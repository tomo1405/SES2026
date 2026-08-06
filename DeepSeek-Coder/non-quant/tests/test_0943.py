import pytest
from src_0943 import task_func

def test_task_func():
    result = task_func()
    assert isinstance(result, tuple), "The function should return a tuple."
    sales_df, ax = result
    assert isinstance(sales_df, pd.DataFrame), "The first element of the tuple should be a DataFrame."
    assert isinstance(ax, plt.Axes), "The second element of the tuple should be a matplotlib Axes object."
    assert len(sales_df) > 0, "The DataFrame should not be empty."
    assert len(sales_df['Date'].unique()) == len(sales_df), "The 'Date' column should be unique."
    assert all(sales_df['Sales'] > 0), "The 'Sales' column should contain positive values."
    assert all(sales_df['Category'].isin(CATEGORIES)), "All categories should be in the allowed categories."