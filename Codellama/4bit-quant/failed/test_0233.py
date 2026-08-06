import pytest
from src_0233 import task_func

def test_task_func():
    df = pd.DataFrame({'Customer': ['Alice', 'Bob', 'Charlie'],
                       'Sales': [100, 200, 300],
                       'Category': ['Toys', 'Toys', 'Electronics']})
    result = task_func(df)
    assert result['Total Sales'] == 600
    assert result['Most Popular Category'] == 'Toys'

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(123)