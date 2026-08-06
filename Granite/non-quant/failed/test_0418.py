import pytest
from src_0418 import task_func

def test_task_func():
    X = [[0, 0], [0, 1], [1, 0], [1, 1]]
    Y = [0, 1, 1, 0]
    model, ax = task_func(X, Y)
    assert model.loss == 'binary_crossentropy'
    assert ax.get_title() == 'Model loss'
    assert ax.get_ylabel() == 'Loss'
    assert ax.get_xlabel() == 'Epoch'
    assert ax.lines[0].get_label() == 'Train Loss'
    assert ax.lines[1].get_label() == 'Validation Loss'