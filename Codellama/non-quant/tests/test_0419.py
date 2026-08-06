import pytest
from src_0419 import task_func

def test_task_func():
    X = [[1, 2], [3, 4], [5, 6], [7, 8]]
    Y = [0, 1, 1, 0]
    model, ax = task_func(X, Y)
    assert isinstance(model, keras.Sequential)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert len(ax.lines) == 2
    assert ax.lines[0].get_xdata() == [0, 1]
    assert ax.lines[0].get_ydata() == [0, 1]
    assert ax.lines[1].get_xdata() == fpr
    assert ax.lines[1].get_ydata() == tpr
    assert ax.get_xlabel() == 'False positive rate'
    assert ax.get_ylabel() == 'True positive rate'
    assert ax.get_title() == 'ROC curve'
    assert ax.get_legend() == 'AUC = {:.3f}'.format(auc_score)