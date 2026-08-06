import pandas as pd
import numpy as np
import itertools
from datetime import datetime, timedelta
import seaborn as sns
from src_0076 import task_func
import pytest

def test_input_type():
    with pytest.raises(TypeError):
        task_func("not a DataFrame")

def test_input_empty():
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())

def test_sales_bounds():
    with pytest.raises(ValueError):
        task_func(pd.DataFrame(), sales_lower_bound=50, sales_upper_bound=1)

def test_output_type():
    df, plot = task_func(pd.DataFrame())
    assert isinstance(df, pd.DataFrame)
    assert isinstance(plot, sns.axisgrid.BoxPlot)

def test_fruits_days():
    df, plot = task_func(pd.DataFrame())
    assert df['Fruit'].tolist() == ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
    assert df['Day'].dt.date.tolist() == [datetime(2024, 1, 1).date(), datetime(2024, 1, 2).date(), datetime(2024, 1, 3).date(), datetime(2024, 1, 4).date(), datetime(2024, 1, 5).date(), datetime(2024, 1, 6).date(), datetime(2024, 1, 7).date()]

def test_sales_values():
    df, plot = task_func(pd.DataFrame())
    assert (df['Sales'] >= 1).all() and (df['Sales'] <= 50).all()