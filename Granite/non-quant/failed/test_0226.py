import pandas as pd
import matplotlib.pyplot as plt
import pytest
from src_0226 import task_func

@pytest.fixture
def sample_df():
    return pd.DataFrame({'A': range(1, 101), 'B': range(101, 201)})

@pytest.fixture
def sample_dct():
    return {'A': 100, 'B': 150}

def test_input_df_type(sample_df, sample_dct):
    with pytest.raises(ValueError) as excinfo:
        task_func(123, sample_dct)
    assert "The input df is not a DataFrame" in str(excinfo.value)

def test_replace_values(sample_df, sample_dct):
    df_replaced = task_func(sample_df, sample_dct)
    assert df_replaced['A'].max() != 100
    assert df_replaced['B'].max() != 150

def test_plot_histograms(sample_df, sample_dct):
    with pytest.raises(ValueError) as excinfo:
        task_func(sample_df, sample_dct, plot_histograms=True)
    assert "columns must be specified" in str(excinfo.value)

    df_replaced = task_func(sample_df, sample_dct, columns=['A'], plot_histograms=True)
    assert len(plt.get_fignums()) == 1