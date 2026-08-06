import pytest
from src_0641 import task_func

def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (12, 5)
    assert all(df.index == MONTHS)
    assert all(df.columns == PRODUCTS)
    assert all(df.values >= 100)
    assert all(df.values <= 1001)

def test_visualizations():
    df = task_func()
    total_sales = df.sum()
    assert isinstance(total_sales, pd.Series)
    assert total_sales.name == 'Total Sales'
    assert total_sales.index == PRODUCTS
    assert all(total_sales.values >= 100)
    assert all(total_sales.values <= 1001)

    heatmap = sns.heatmap(df, annot=True, fmt="d", cmap='viridis')
    assert isinstance(heatmap, sns.heatmap)
    assert heatmap.shape == (12, 5)
    assert all(heatmap.index == MONTHS)
    assert all(heatmap.columns == PRODUCTS)
    assert all(heatmap.values >= 100)
    assert all(heatmap.values <= 1001)