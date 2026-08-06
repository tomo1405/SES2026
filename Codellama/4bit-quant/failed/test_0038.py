import pytest
from src_0038 import task_func

def test_task_func():
    df = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6], 'target': [0, 1, 0]})
    target_column = 'target'
    model, ax = task_func(df, target_column)
    assert isinstance(model, RandomForestClassifier)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_xlabel() == "Feature Importance Score"
    assert ax.get_ylabel() == "Features"
    assert ax.get_title() == "Visualizing Important Features"
    assert len(ax.get_xticks()) == 2
    assert len(ax.get_yticks()) == 3
    assert ax.get_xticks()[0] == 0.5
    assert ax.get_xticks()[1] == 1.5
    assert ax.get_yticks()[0] == "feature1"
    assert ax.get_yticks()[1] == "feature2"
    assert ax.get_yticks()[2] == "target"