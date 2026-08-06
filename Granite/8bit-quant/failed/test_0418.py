import pytest
from src_0418 import task_func

def test_task_func():
    X = # your input data
    Y = # your target data
    model, ax = task_func(X, Y)
    assert model.loss == 'binary_crossentropy'
    assert ax.title == 'Model loss'
    assert ax.ylabel == 'Loss'
    assert ax.xlabel == 'Epoch'
    assert ax.legend == ['Train', 'Test']