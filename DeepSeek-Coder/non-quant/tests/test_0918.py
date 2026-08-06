import pytest
from src_0918 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from statsmodels.tsa.arima.model import ARIMA
from typing import List, Tuple

# Assuming src_0918 contains the target function

def test_task_func():
    # Create a sample DataFrame for testing
    data = {
        'date': pd.date_range(start='2023-01-01', periods=100),
        'closing_price': range(100, 200)
    }
    df = pd.DataFrame(data)

    # Call the function
    forecast, ax = task_func(df=df)

    # Add assertions to verify the output
    assert isinstance(forecast, list), "The forecast should be a list"
    assert isinstance(ax, Axes), "The plot axis should be an instance of Axes"
    assert len(forecast) == 7, "The forecast should contain 7 days of forecasts"