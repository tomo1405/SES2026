import pytest
from src_0915 import task_func

def test_task_func():
    # Test data
    df = pd.DataFrame({'date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
                   'closing_price': [100, 105, 110, 115, 120]})
    
    # Test function
    pred_prices, ax = task_func(df)
    
    # Assertions
    assert pred_prices == [105, 110, 115, 120, 125, 130, 135, 140]
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Closing Price'
    assert ax.get_title() == 'Stock Price Prediction'