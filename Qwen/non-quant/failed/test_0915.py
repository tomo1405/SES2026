import pytest
from src_0915 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

@pytest.fixture
def sample_data():
    dates = pd.date_range(start='2023-01-01', periods=5, freq='D')
    closing_prices = [100, 102, 101, 105, 107]
    df = pd.DataFrame({'date': dates, 'closing_price': closing_prices})
    return df

def test_task_func_output(sample_data):
    pred_prices, ax = task_func(sample_data)
    assert isinstance(pred_prices, list)
    assert len(pred_prices) == 7
    assert all(isinstance(price, float) for price in pred_prices)
    assert isinstance(ax, plt.Axes)

def test_task_func_plot(sample_data, monkeypatch):
    def mock_scatter(x, y, color):
        assert len(x) == 5
        assert len(y) == 5
        assert color == 'black'
    
    def mock_plot(x, y, color, linewidth):
        assert len(x) == 7
        assert len(y) == 7
        assert color == 'blue'
        assert linewidth == 3
    
    monkeypatch.setattr(plt.Axes, 'scatter', mock_scatter)
    monkeypatch.setattr(plt.Axes, 'plot', mock_plot)
    
    task_func(sample_data)

def test_task_func_dates_conversion(sample_data):
    original_dates = sample_data['date'].copy()
    task_func(sample_data)
    converted_dates = sample_data['date']
    assert not np.array_equal(original_dates, converted_dates)
    assert all(isinstance(date, np.float64) for date in converted_dates)