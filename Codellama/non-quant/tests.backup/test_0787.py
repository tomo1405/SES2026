import pytest
from src_0787 import task_func

def test_task_func():
    # Test with default values
    df = task_func(n=10)
    assert len(df) == 10
    assert set(df.columns) == {'Country', 'Product', 'Sales'}
    assert all(df['Sales'] >= 1) and all(df['Sales'] <= 100)

    # Test with custom values
    df = task_func(n=10, countries=['USA', 'UK', 'China'], products=['Product A', 'Product B', 'Product C'])
    assert len(df) == 10
    assert set(df.columns) == {'Country', 'Product', 'Sales'}
    assert all(df['Country'].isin(['USA', 'UK', 'China']))
    assert all(df['Product'].isin(['Product A', 'Product B', 'Product C']))
    assert all(df['Sales'] >= 1) and all(df['Sales'] <= 100)

    # Test with output path
    output_path = 'test_output.csv'
    df = task_func(n=10, output_path=output_path)
    assert len(df) == 10
    assert set(df.columns) == {'Country', 'Product', 'Sales'}
    assert all(df['Sales'] >= 1) and all(df['Sales'] <= 100)
    assert os.path.exists(output_path)
    os.remove(output_path)

    # Test with random seed
    df1 = task_func(n=10, random_seed=123)
    df2 = task_func(n=10, random_seed=123)
    assert df1.equals(df2)