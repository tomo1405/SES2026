import numpy as np
import pandas as pd


def test_task_func():
    # Create a sample dataframe
    df = pd.DataFrame({'date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
                   'closing_price': [100, 110, 120, 130, 140]})
    
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
    
    # Test that the function returns the correct values
    assert pred_prices.tolist() == [100, 110, 120, 130, 140, 150, 160, 170]
    
    # Test that the plot is created correctly
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)