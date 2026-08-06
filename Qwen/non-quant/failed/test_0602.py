import pytest
from src_0602 import task_func
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {'Word': ['apple', 'banana', 'cherry', 'date', 'elderberry']}
    return pd.DataFrame(data)

@pytest.fixture
def empty_df():
    return pd.DataFrame()

def test_task_func_with_valid_data(sample_df):
    ax = task_func(sample_df, 'a')
    assert isinstance(ax, sns.axisgrid.AxesSubplot)
    plt.close(ax.figure)

def test_task_func_with_no_matching_words(sample_df):
    ax = task_func(sample_df, 'z')
    assert ax is None

def test_task_func_with_empty_dataframe(empty_df):
    ax = task_func(empty_df, 'a')
    assert ax is None

def test_task_func_missing_word_column(sample_df):
    del sample_df['Word']
    with pytest.raises(ValueError) as excinfo:
        task_func(sample_df, 'a')
    assert str(excinfo.value) == "The DataFrame should contain a 'Word' column."

def test_task_func_performance(sample_df):
    start_time = time.time()
    ax = task_func(sample_df, 'a')
    end_time = time.time()
    assert isinstance(ax, sns.axisgrid.AxesSubplot)
    assert (end_time - start_time) < 1  # Ensure the operation completes quickly
    plt.close(ax.figure)