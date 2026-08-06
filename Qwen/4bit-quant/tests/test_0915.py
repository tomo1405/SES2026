import matplotlib.pyplot as plt
import pandas as pd
import pytest
from src_0915 import task_func


@pytest.fixture
def sample_data():
    data = {
        'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'closing_price': [100, 102, 101]
    }
    return pd.DataFrame(data)

def test_task_func(sample_data):
    predicted_prices, ax = task_func(sample_data)
    
    # Check if the number of predicted prices is correct
    assert len(predicted_prices) == 7, "The number of predicted prices should be 7."
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object."
    
    # Check if the predicted prices are within a reasonable range
    min_price = sample_data['closing_price'].min()
    max_price = sample_data['closing_price'].max()
    assert all(min_price <= price <= max_price for price in predicted_prices), "Predicted prices should be within the range of the input data."

def test_task_func_with_empty_data():
    empty_df = pd.DataFrame(columns=['date', 'closing_price'])
    with pytest.raises(ValueError):
        task_func(empty_df)

def test_task_func_with_missing_columns():
    incomplete_df = pd.DataFrame({'date': ['2023-01-01']})
    with pytest.raises(KeyError):
        task_func(incomplete_df)