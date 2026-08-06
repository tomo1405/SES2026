import pytest
from src_0299 import task_func
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import io

def test_task_func_basic():
    data = {
        'Date': ['2023-01-01', '2023-01-02'],
        'Value': [[1, 2], [3, 4]]
    }
    df = pd.DataFrame(data)
    result = task_func(df)
    assert isinstance(result, pd.DataFrame)
    assert all(result.columns == ['Date', 0, 1])
    assert len(result) == 2

def test_task_func_plot():
    data = {
        'Date': ['2023-01-01', '2023-01-02'],
        'Value': [[1, 2], [3, 4]]
    }
    df = pd.DataFrame(data)
    buffer = io.BytesIO()
    plt.switch_backend('Agg')
    plt.savefig(buffer)
    result, ax = task_func(df, plot=True)
    assert isinstance(result, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert all(result.columns == ['Date', 0, 1])
    assert len(result) == 2

def test_task_func_with_invalid_date():
    data = {
        'Date': ['invalid-date', '2023-01-02'],
        'Value': [[1, 2], [3, 4]]
    }
    df = pd.DataFrame(data)
    with pytest.raises(pd.errors.ParserError):
        task_func(df)

def test_task_func_with_empty_dataframe():
    df = pd.DataFrame(columns=['Date', 'Value'])
    result = task_func(df)
    assert result.empty