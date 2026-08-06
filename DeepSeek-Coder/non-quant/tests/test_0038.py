import pytest
from src_0038 import task_func
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

@pytest.fixture
def sample_data():
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'target': [0, 1, 0, 1, 0]
    }
    return pd.DataFrame(data)

def test_task_func(sample_data):
    df = sample_data
    target_column = 'target'
    model, ax = task_func(df=df, target_column=target_column)
    
    assert isinstance(model, RandomForestClassifier)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) > 0