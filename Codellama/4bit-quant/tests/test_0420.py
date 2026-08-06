import pytest
from src_0420 import task_func
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve
from tensorflow import keras
import matplotlib.pyplot as plt

def test_task_func():
    X = ...  # Generate some data
    Y = ...  # Generate some labels
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)
    input_dim = X.shape[1]

    model, ax = task_func(X_train, Y_train)

    assert isinstance(model, keras.models.Sequential)
    assert isinstance(ax, plt.Axes)

    Y_pred = model.predict(X_test, verbose=0).ravel()
    precision, recall, thresholds = precision_recall_curve(Y_test, Y_pred)

    assert precision.shape == (len(thresholds),)
    assert recall.shape == (len(thresholds),)
    assert thresholds.shape == (len(thresholds),)

    assert ax.get_xlabel() == 'Recall'
    assert ax.get_ylabel() == 'Precision'
    assert ax.get_title() == 'Precision-Recall Curve'
    assert ax.get_legend() == 'Precision-Recall curve'

    plt.close(fig)