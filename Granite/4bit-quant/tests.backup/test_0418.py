import pytest
from src_0418 import task_func

def test_task_func():
    # Mock input data
    X = [[0, 0], [0, 1], [1, 0], [1, 1]]
    Y = [0, 1, 1, 0]

    # Call the function
    model, ax = task_func(X, Y)

    # Assert the outputs
    assert model.loss == 'binary_crossentropy'
    assert ax.title.get_text() == 'Model loss'
    assert ax.legend()[0].get_text() == 'Train'
    assert ax.legend()[1].get_text() == 'Test'