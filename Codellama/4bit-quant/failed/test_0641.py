import pytest
from src_0641 import task_func

def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (len(MONTHS), len(PRODUCTS))
    assert df.index.equals(MONTHS)
    assert df.columns.equals(PRODUCTS)
    assert np.all(df >= 0)
    assert np.all(df <= 1001)

def test_total_sales():
    df = task_func()
    total_sales = df.sum()
    assert isinstance(total_sales, pd.Series)
    assert total_sales.index.equals(PRODUCTS)
    assert np.all(total_sales >= 0)
    assert np.all(total_sales <= 1001)

def test_heatmap():
    df = task_func()
    heatmap = sns.heatmap(df, annot=True, fmt="d", cmap='viridis')
    assert isinstance(heatmap, matplotlib.axes.Axes)
    assert heatmap.shape == (len(MONTHS), len(PRODUCTS))
    assert np.all(heatmap >= 0)
    assert np.all(heatmap <= 1001)