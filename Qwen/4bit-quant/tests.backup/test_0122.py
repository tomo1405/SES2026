import pytest
from src_0122 import task_func
import pandas as pd
import numpy as np

def test_task_func_input_type():
    with pytest.raises(TypeError):
        task_func("not_a_list")

def test_task_func_output_type():
    result_df, result_ax = task_func([1, 2, 3])
    assert isinstance(result_df, pd.DataFrame)
    assert result_ax is not None

def test_task_func_append_value():
    result_df, _ = task_func([1, 2, 3])
    assert result_df.iloc[-1]['Sales'] == 12 * np.random.randint(100, 1000)

def test_task_func_categories():
    result_df, _ = task_func([1, 2, 3])
    assert all(category in result_df['Category'].values for category in ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports'])

def test_task_func_randomness():
    df1, _ = task_func([1, 2, 3], seed=42)
    df2, _ = task_func([1, 2, 3], seed=42)
    assert df1.equals(df2)

def test_task_func_plot_title():
    _, ax = task_func([1, 2, 3])
    assert ax.get_title() == 'Category-wise Sales Data'

def test_task_func_plot_ylabel():
    _, ax = task_func([1, 2, 3])
    assert ax.get_ylabel() == 'Sales'