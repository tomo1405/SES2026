import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from src_0970 import task_func
import pytest

@pytest.fixture
def input_df():
    return pd.DataFrame({
        'A': np.random.rand(100),
        'B': np.random.rand(100),
        'C': np.random.randint(1, 100, 100)
    })

def test_task_func_input_types(input_df):
    with pytest.raises(TypeError):
        task_func(input_df.astype(str))

def test_task_func_input_values(input_df):
    with pytest.raises(ValueError):
        task_func(input_df.mask(np.random.rand(100, 3) > 0.5))

def test_task_func_output_types(input_df):
    output_df = task_func(input_df)
    assert output_df.dtypes.apply(lambda x: x.name).tolist() == ['float64'] * 3

def test_task_func_output_range(input_df):
    output_df = task_func(input_df)
    assert (output_df.min() >= 0).all() and (output_df.max() <= 1).all()