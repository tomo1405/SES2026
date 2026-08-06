import pytest
from src_0418 import task_func

def test_task_func():
    X = [[1, 2], [3, 4], [5, 6], [7, 8]]
    Y = [0, 1, 1, 0]
    model, ax = task_func(X, Y)
    assert isinstance(model, Sequential)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert len(model.layers) == 1
    assert model.layers[0].units == 1
    assert model.layers[0].activation == 'sigmoid'
    assert model.optimizer == SGD(learning_rate=0.1)
    assert model.loss == 'binary_crossentropy'
    assert model.metrics == ['accuracy']
    assert model.compile(loss='binary_crossentropy', optimizer=SGD(learning_rate=0.1))
    assert model.fit(X_train, Y_train, epochs=200, batch_size=1, verbose=0, validation_data=(X_test, Y_test))
    assert len(history.history['loss']) == 200
    assert len(history.history['val_loss']) == 200
    assert len(history.history['accuracy']) == 200
    assert len(history.history['val_accuracy']) == 200
    assert len(ax.lines) == 2
    assert ax.lines[0].get_label() == 'Train Loss'
    assert ax.lines[1].get_label() == 'Validation Loss'
    assert ax.get_title() == 'Model loss'
    assert ax.get_ylabel() == 'Loss'
    assert ax.get_xlabel() == 'Epoch'
    assert ax.get_legend() == ['Train', 'Test']