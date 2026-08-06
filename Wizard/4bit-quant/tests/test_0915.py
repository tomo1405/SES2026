python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pytest

def task_func(df):
    # Convert date to timestamp
    df['date'] = pd.to_datetime(df['date'])
    df['date'] = df['date'].map(pd.Timestamp.timestamp)
    
    # Prepare data
    X = df['date'].values.reshape(-1, 1)
    y = df['closing_price'].values
    
    # Fit model
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict future prices
    future_dates = np.array([df['date'].max() + i*24*60*60 for i in range(1, 8)]).reshape(-1, 1)
    pred_prices = model.predict(future_dates)
    
    # Plot
    fig, ax = plt.subplots()
    ax.scatter(df['date'], df['closing_price'], color='black')
    ax.plot(future_dates, pred_prices, color='blue', linewidth=3)
    
    return pred_prices.tolist(), ax

def test_task_func():
    # Test case 1: normal input
    df = pd.DataFrame({'date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05'], 'closing_price': [100, 105, 110, 115, 120]})
    pred_prices, ax = task_func(df)
    assert len(pred_prices) == 7
    assert ax.get_xlabel() == 'date'
    assert ax.get_ylabel() == 'closing_price'
    assert ax.get_title() == 'Predictions'
    assert ax.get_lines()[0].get_color() == 'blue'
    assert ax.get_lines()[0].get_linewidth() == 3
    
    # Test case 2: empty dataframe
    df = pd.DataFrame({'date': [], 'closing_price': []})
    pred_prices, ax = task_func(df)
    assert len(pred_prices) == 0
    assert ax.get_xlabel() == 'date'
    assert ax.get_ylabel() == 'closing_price'
    assert ax.get_title() == 'Predictions'
    assert ax.get_lines()[0].get_color() == 'blue'
    assert ax.get_lines()[0].get_linewidth() == 3
    
    # Test case 3: missing column
    df = pd.DataFrame({'date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05']})
    with pytest.raises(KeyError):
        pred_prices, ax = task_func(df)
    
    # Test case 4: invalid date format
    df = pd.DataFrame({'date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05'], 'closing_price': [100, 105, 110, 115, 120]})
    df.loc[0, 'date'] = '2021-01-01 00:00:00'
    with pytest.raises(ValueError):
        pred_prices, ax = task_func(df)