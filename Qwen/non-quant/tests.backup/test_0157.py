import pytest
from src_0157 import task_func
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import numpy as np

@pytest.fixture
def sample_data():
    # Create a sample DataFrame with random values
    data = np.random.rand(10, 8)  # 10 samples, 8 features
    df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
    return df.values

def test_task_func_output(sample_data):
    df, ax = task_func(sample_data)
    
    # Check if the returned DataFrame has the correct shape
    assert df.shape == (10, 9), "The DataFrame should have 10 rows and 9 columns."
    
    # Check if the 'Average' column is present
    assert 'Average' in df.columns, "The DataFrame should have an 'Average' column."
    
    # Check if the 'Average' column contains the correct values
    expected_average = df.iloc[:, :8].mean(axis=1)
    assert df['Average'].equals(expected_average), "The 'Average' column values are incorrect."
    
    # Check if the plot axis is of the correct type
    assert isinstance(ax, plt.Axes), "The returned object should be a matplotlib Axes instance."

def test_task_func_plot(sample_data, mocker):
    # Mock the plt.subplots function to capture the figure and axes
    mock_fig, mock_ax = plt.subplots()
    mocker.patch('matplotlib.pyplot.subplots', return_value=(mock_fig, mock_ax))
    
    df, ax = task_func(sample_data)
    
    # Check if the plot method was called on the 'Average' column
    mock_ax.plot.assert_called_once_with(df['Average'])

def test_task_func_column_names(sample_data):
    df, _ = task_func(sample_data)
    
    # Check if the DataFrame has the correct column names
    expected_columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'Average']
    assert list(df.columns) == expected_columns, "The DataFrame should have the correct column names."