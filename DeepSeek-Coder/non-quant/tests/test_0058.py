import pytest
from src_0058 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@pytest.fixture
def sample_data():
    data = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [2, 3, 4, 5, 6]
    })
    return data

def test_task_func(sample_data):
    csv_file_path = 'sample_data.csv'
    title = 'Test Correlation Heatmap'
    corr, _ = task_func(csv_file_path=csv_file_path, title=title)
    
    assert isinstance(corr, pd.DataFrame), "The result should be a DataFrame"
    assert len(corr) > 0, "The correlation matrix should not be empty"
    assert plt.gca() is not None, "The plot should be created"