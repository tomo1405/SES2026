import pytest
from src_0038 import task_func
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'target': [0, 1, 0, 1, 0]
    }
    return pd.DataFrame(data)

def test_task_func_output_type(sample_df):
    model, ax = task_func(sample_df, 'target')
    assert isinstance(model, RandomForestClassifier)
    assert isinstance(ax, plt.Axes)

def test_task_func_feature_importance(sample_df):
    model, ax = task_func(sample_df, 'target')
    feature_imp = pd.Series(model.feature_importances_, index=sample_df.drop('target', axis=1).columns).sort_values(ascending=False)
    assert not feature_imp.empty

def test_task_func_plot_labels(sample_df):
    model, ax = task_func(sample_df, 'target')
    assert ax.get_xlabel() == "Feature Importance Score"
    assert ax.get_ylabel() == "Features"
    assert ax.get_title() == "Visualizing Important Features"

def test_task_func_plot_data(sample_df):
    model, ax = task_func(sample_df, 'target')
    bars = ax.patches
    assert len(bars) == len(sample_df.drop('target', axis=1).columns)