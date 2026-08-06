import pytest
from src_0420 import task_func

def test_task_func():
    X = [[1, 2], [3, 4], [5, 6], [7, 8]]
    Y = [0, 1, 0, 1]
    model, ax = task_func(X, Y)
    assert model is not None
    assert ax is not None
    assert ax.get_xlabel() == 'Recall'
    assert ax.get_ylabel() == 'Precision'
    assert ax.get_title() == 'Precision-Recall Curve'
    assert ax.legend()[0].get_label() == 'Precision-Recall curve'