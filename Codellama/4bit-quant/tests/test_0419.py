import pytest
from src_0419 import task_func
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

def test_task_func():
    X = [[1, 2], [3, 4], [5, 6], [7, 8]]
    Y = [0, 1, 1, 0]
    model, ax = task_func(X, Y)
    assert isinstance(model, keras.Sequential)
    assert isinstance(ax, plt.Axes)
    assert model.layers[0].input_dim == 2
    assert model.layers[0].units == 1
    assert model.layers[0].activation == 'sigmoid'
    assert model.loss == 'binary_crossentropy'
    assert isinstance(model.optimizer, keras.optimizers.SGD)
    assert model.optimizer.learning_rate == 0.1
    assert model.fit(X, Y, epochs=200, batch_size=1, verbose=0)
    Y_pred = model.predict(X, verbose=0).ravel()
    fpr, tpr, thresholds = roc_curve(Y, Y_pred)
    auc_score = auc(fpr, tpr)
    assert fpr.shape == (2,)
    assert tpr.shape == (2,)
    assert thresholds.shape == (2,)
    assert auc_score > 0
    assert ax.get_xlabel() == 'False positive rate'
    assert ax.get_ylabel() == 'True positive rate'
    assert ax.get_title() == 'ROC curve'
    assert ax.get_legend() == 'AUC = {:.3f}'.format(auc_score)