import pytest
from src_0038 import task_func
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt

def test_task_func():
    df = pd.DataFrame({'feature1': [1, 2, 3, 4, 5], 'feature2': [6, 7, 8, 9, 10], 'target': [0, 1, 0, 1, 0]})
    target_column = 'target'
    model, ax = task_func(df, target_column)
    assert isinstance(model, RandomForestClassifier)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == "Feature Importance Score"
    assert ax.get_ylabel() == "Features"
    assert ax.get_title() == "Visualizing Important Features"
    assert len(ax.get_xticks()) == 2
    assert len(ax.get_yticks()) == 2
    assert ax.get_xticks()[0] == 1
    assert ax.get_xticks()[1] == 2
    assert ax.get_yticks()[0] == "feature1"
    assert ax.get_yticks()[1] == "feature2"