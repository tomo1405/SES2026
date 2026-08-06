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

# Define a sample input DataFrame for testing
test_df = pd.DataFrame({
    'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'closing_price': [100, 110, 120, 130, 140]
})

# Define the expected output for the test input
expected_pred_prices = [144.0, 156.0, 168.0, 180.0, 192.0, 204.0, 216.0]
expected_ax_plot = None  # You can add an assertion for the plot if needed

# Write the test case
def test_task_func():
    pred_prices, ax = task_func(test_df)
    assert pred_prices == expected_pred_prices
    assert ax == expected_ax_plot

# Run the test case
pytest.main()