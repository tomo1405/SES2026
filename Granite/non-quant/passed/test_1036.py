import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
def task_func(feature: pd.Series, target: pd.Series) -> (np.ndarray, plt.Axes):
    df = pd.DataFrame({"Feature": feature, "Target": target})
    X_train, X_test, y_train, y_test = train_test_split(
        df["Feature"], df["Target"], test_size=0.2, random_state=42
    )
    model = LogisticRegression()
    model.fit(X_train.values.reshape(-1, 1), y_train)
    y_pred = model.predict(X_test.values.reshape(-1, 1))
    cm = confusion_matrix(y_test, y_pred)
    _, ax = plt.subplots()
    cax = ax.matshow(cm, cmap="Blues")
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.colorbar(cax)
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_xticklabels(["No", "Yes"])
    ax.set_yticklabels(["No", "Yes"])
    return cm, ax
import pytest

def test_task_func():
    feature = pd.Series([1, 0, 1, 0, 1, 0, 0, 1])
    target = pd.Series([1, 0, 1, 0, 1, 0, 0, 1])
    expected_cm = np.array([[4, 0], [0, 4]])
    expected_ax = None  # You can't easily compare matplotlib Axes objects
    cm, ax = task_func(feature, target)
    assert np.array_equal(cm, expected_cm)
    assert ax is expected_ax

if __name__ == "__main__":
    pytest.main()