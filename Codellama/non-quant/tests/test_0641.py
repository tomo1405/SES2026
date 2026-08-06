import pandas as pd
from src_0641 import task_func


def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (12, 5)
    assert all(df.columns == PRODUCTS)
    assert all(df.index == MONTHS)
    assert all(df.dtypes == np.int64)
    assert all(df.values >= 100)
    assert all(df.values <= 1000)

    total_sales = df.sum()
    assert isinstance(total_sales, pd.Series)
    assert total_sales.shape == (5,)
    assert all(total_sales.index == PRODUCTS)
    assert all(total_sales.values >= 100)
    assert all(total_sales.values <= 1000)

    plt.figure(figsize=(10, 5))
    total_sales.plot(kind='line', title='Total Sales per Product')
    plt.ylabel('Total Sales')
    plt.show()

    plt.figure(figsize=(10, 8))
    sns.heatmap(df, annot=True, fmt="d", cmap='viridis')
    plt.title('Monthly Sales per Product')
    plt.show()