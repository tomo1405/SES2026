import pytest
from src_0076 import task_func

def test_input_type():
    df = pd.DataFrame()
    with pytest.raises(TypeError):
        task_func(df, fruits=None, days=None, seed=None, sales_lower_bound=1, sales_upper_bound=50)

def test_input_empty():
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df, fruits=None, days=None, seed=None, sales_lower_bound=1, sales_upper_bound=50)

def test_sales_bounds():
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df, fruits=None, days=None, seed=None, sales_lower_bound=50, sales_upper_bound=1)

def test_fruits():
    df = pd.DataFrame()
    result_df, plot = task_func(df, fruits=['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'], days=None, seed=None, sales_lower_bound=1, sales_upper_bound=50)
    assert result_df.columns.tolist() == ['Fruit', 'Day', 'Sales']
    assert result_df['Fruit'].tolist() == ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']

def test_days():
    df = pd.DataFrame()
    result_df, plot = task_func(df, fruits=None, days=[datetime(2024, 1, 1) + timedelta(days=x) for x in range(7)], seed=None, sales_lower_bound=1, sales_upper_bound=50)
    assert result_df.columns.tolist() == ['Fruit', 'Day', 'Sales']
    assert result_df['Day'].tolist() == [datetime(2024, 1, 1) + timedelta(days=x) for x in range(7)]

def test_seed():
    df = pd.DataFrame()
    result_df, plot = task_func(df, fruits=None, days=None, seed=1234, sales_lower_bound=1, sales_upper_bound=50)
    assert result_df.columns.tolist() == ['Fruit', 'Day', 'Sales']
    assert result_df['Sales'].tolist() == [1, 2, 3, 4, 5, 6, 7]

def test_sales_data():
    df = pd.DataFrame()
    result_df, plot = task_func(df, fruits=None, days=None, seed=None, sales_lower_bound=1, sales_upper_bound=50)
    assert result_df.columns.tolist() == ['Fruit', 'Day', 'Sales']
    assert result_df['Sales'].tolist() == [1, 2, 3, 4, 5, 6, 7]