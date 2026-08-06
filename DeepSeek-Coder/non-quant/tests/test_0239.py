import pytest
from src_0239 import task_func
import matplotlib
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pandas as pd

@pytest.fixture
def sample_data():
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Score': [70, 80, 85, 90]
    }
    return pd.DataFrame(data)

def test_task_func(sample_data):
    df = sample_data
    result, _ = task_func(df)
    
    assert isinstance(result, tuple), "The function should return a tuple."
    assert len(result) == 2, "The function should return a tuple with two elements."
    
    df, ax = result
    assert isinstance(df, pd.DataFrame), "The first element of the tuple should be a DataFrame."
    assert isinstance(ax, plt.Axes), "The second element of the tuple should be a matplotlib Axes object."
    
    assert len(df) == 4, "The DataFrame should have the correct number of rows."
    assert 'Age_scaled' in df.columns and 'Score_scaled' in df.columns, "The DataFrame should have scaled Age and Score columns."
    assert df['Age_scaled'].min() >= -1 and df['Age_scaled'].max() <= 1, "The Age column should be standardized."
    assert df['Score_scaled'].min() >= -1 and df['Score_scaled'].max() <= 1, "The Score column should be standardized."
    
    plt.close()  # Close the plot to avoid hanging tests