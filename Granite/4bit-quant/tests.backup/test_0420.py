import pytest
from src_0420 import task_func

def test_task_func():
    X = # your input data
    Y = # your target data
    model, ax = task_func(X, Y)
    assert model is not None, "model should not be None"
    assert ax is not None, "ax should not be None"
    assert ax.get_xlabel() == 'Recall', "xlabel should be 'Recall'"
    assert ax.get_ylabel() == 'Precision', "ylabel should be 'Precision'"
    assert ax.get_title() == 'Precision-Recall Curve', "title should be 'Precision-Recall Curve'"
    assert ax.legend()[0].get_text() == 'Precision-Recall curve', "legend should be 'Precision-Recall curve'"