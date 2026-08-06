import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from typing import List, Tuple

def task_func(df: pd.DataFrame) -> Tuple[List[float], plt.Axes]:
    model = ARIMA(df['closing_price'], order=(5, 1, 0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=7)
    fig, ax = plt.subplots()
    ax.plot(df['date'], df['closing_price'], label='Historical Closing Prices')
    forecast_dates = pd.date_range(start=df['date'].iloc[-1] + pd.Timedelta(days=1), periods=7)
    ax.plot(forecast_dates, forecast, label='Forecasted Closing Prices')
    ax.legend()
    return forecast.tolist(), ax

def test_task_func():
    # Test data
    df = pd.DataFrame({
        'date': pd.date_range(start='2023-01-01', periods=10),
        'closing_price': [100, 110, 120, 130, 140, 150, 160, 170, 180, 190]
    })

    # Expected output
    expected_forecast = [191.4124579124579, 193.01190476190476, 194.6113516113516, 196.21079846079847, 197.8102453102453, 199.40969215969216, 201.009139009139]
    expected_ax_line1_ydata = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190]
    expected_ax_line2_ydata = [191.4124579124579, 193.01190476190476, 194.6113516113516, 196.21079846079847, 197.8102453102453, 199.40969215969216, 201.009139009139]

    # Call the function
    forecast, ax = task_func(df)

    # Assert the forecast and ax.lines data
    assert forecast == expected_forecast
    assert ax.lines[0].get_ydata().tolist() == expected_ax_line1_ydata
    assert ax.lines[1].get_ydata().tolist() == expected_ax_line2_ydata