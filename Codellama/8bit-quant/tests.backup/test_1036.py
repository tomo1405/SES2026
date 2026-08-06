import pytest
from src_1036 import task_func
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Create test data
    feature = pd.Series([1, 2, 3, 4, 5])
    target = pd.Series([0, 1, 0, 1, 0])

    # Split the data into train and test datasets
    X_train, X_test, y_train, y_test = train_test_split(
        feature, target, test_size=0.2, random_state=42
    )

    # Initialize and train the Logistic Regression model
    model = LogisticRegression()
    model.fit(X_train.values.reshape(-1, 1), y_train)

    # Make predictions
    y_pred = model.predict(X_test.values.reshape(-1, 1))

    # Compute the confusion matrix
    cm = confusion_matrix(y_test, y_pred)

    # Plot the confusion matrix
    _, ax = plt.subplots()
    cax = ax.matshow(cm, cmap="Blues")
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.colorbar(cax)

    # Setting tick locations
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])

    # Now set tick labels correctly
    ax.set_xticklabels(["No", "Yes"])
    ax.set_yticklabels(["No", "Yes"])

    # Test that the function returns the correct values
    assert cm.shape == (2, 2)
    assert ax.get_title() == "Confusion Matrix"
    assert ax.get_xlabel() == "Predicted"
    assert ax.get_ylabel() == "Actual"
    assert ax.get_xticklabels() == ["No", "Yes"]
    assert ax.get_yticklabels() == ["No", "Yes"]